import customtkinter as ctk
from datetime import datetime
from sqlalchemy import Date, cast, func, cast, Date
from datetime import date
from DB.models import Pedido, Produto, ItemPedido
from DB.Banco import SessionLocal

class DashboardView(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent, fg_color="transparent")
        
        self.grid_columnconfigure((0, 1, 2), weight=1, uniform="group1")
        self.grid_rowconfigure((0, 1), weight=1)

        session = SessionLocal()
        data_referencia = datetime.now().date() #(date) pega o dia mes e ano do meu pc exato
        vendas_dia = (
            session.query(Pedido)
            .filter(Pedido.status == 'FINALIZADO', Pedido.data_hora_fim != None, cast(Pedido.data_hora_fim, Date) == data_referencia).all()
        )
        total_vendas = sum(pedido.valor_final for pedido in vendas_dia if pedido.valor_final)
        
        # Card 1: Vendas do Dia
        c1 = self.create_card(0, 0)
        ctk.CTkLabel(c1, text="VENDAS DO DIA 💰", font=ctk.CTkFont(size=14, weight="bold"), text_color="#000").pack(anchor="w", padx=15, pady=(15, 5))
        ctk.CTkLabel(c1, text=f'R$ {total_vendas:.2f}', font=ctk.CTkFont(size=28, weight="bold"), text_color="#000").pack(anchor="w", padx=15)
        ctk.CTkLabel(c1, text="📈 [Gráfico de Linhas]", font=ctk.CTkFont(size=12), text_color="#888").pack(expand=True)

        resultados_query = (
            session.query(
                Produto.nome.label('nome_produto'),
                func.sum(ItemPedido.quantidade).label('total_quantidade')
            )
            .join(ItemPedido, ItemPedido.fk_id_produto == Produto.id)
            .join(Pedido, ItemPedido.fk_id_pedido == Pedido.id)
            .filter(cast(Pedido.data_hora_inicio, Date) == date.today())
            .group_by(Produto.id, Produto.nome)
            .order_by(func.sum(ItemPedido.quantidade).desc())
            .limit(3)
            .all()
        )

        # Junta os resultados colocando um embaixo do outro usando "\n"
        texto_resultados = "\n".join([f"{i}º  {r.nome_produto} — {r.total_quantidade} un." for i, r in enumerate(resultados_query, 1)])
        # Se não houver vendas hoje, exibe uma mensagem amigável
        if not texto_resultados:
            texto_resultados = "Nenhum pedido registrado hoje."
        
        # Card 2: Top Lanches
        c2 = self.create_card(0, 1)
        # Título do Card
        ctk.CTkLabel(c2, text="TOP LANCHES 🍔", font=ctk.CTkFont(size=14, weight="bold"), text_color="#000").pack(anchor="w", padx=15, pady=(15, 10))
        # Espaço onde antes ficava o gráfico agora é totalmente dedicado à lista (com alinhamento à esquerda)
        ctk.CTkLabel(c2, text=texto_resultados, font=ctk.CTkFont(size=12), text_color="#333", justify="left").pack(anchor="w", padx=20, pady=10, expand=True)

        # Card 3 & 4: Estoque Crítico
        c3 = self.create_card(0, 2)
        self.fill_estoque(c3)

        c4 = self.create_card(1, 0)
        self.fill_estoque(c4)

        # Card 5: Resumo Financeiro
        c5 = self.create_card(1, 1, columnspan=2)
        ctk.CTkLabel(c5, text="RESUMO FINANCEIRO (ÚLTIMOS 7 DIAS)", font=ctk.CTkFont(size=14, weight="bold"), text_color="#000").pack(anchor="w", padx=15, pady=(15, 5))
        ctk.CTkLabel(c5, text="📉 [Área do Gráfico Comparativo]", font=ctk.CTkFont(size=12), text_color="#888").pack(expand=True)

    def create_card(self, row, col, columnspan=1):
        card = ctk.CTkFrame(self, fg_color="#FFFFFF", corner_radius=15, border_width=1, border_color="#E0E0E0")
        card.grid(row=row, column=col, columnspan=columnspan, sticky="nsew", padx=6, pady=6)
        return card

    def fill_estoque(self, card):
        ctk.CTkLabel(card, text="ESTOQUE CRÍTICO 📦", font=ctk.CTkFont(size=14, weight="bold"), text_color="#000").pack(anchor="w", padx=15, pady=(10, 5))
        items = [("🍞 Pão", 0.15, "15 left!", "#D97706"), ("🥩 Carne", 0.35, "20", "#4B5563"), ("🍟 Batata", 0.45, "25", "#4B5563")]
        for name, prog, val, col in items:
            f = ctk.CTkFrame(card, fg_color="transparent")
            f.pack(fill="x", padx=15, pady=2)
            ctk.CTkLabel(f, text=name, font=ctk.CTkFont(size=12, weight="bold"), text_color="#000", width=60, anchor="w").pack(side="left")
            pb = ctk.CTkProgressBar(f, height=8, progress_color=col, fg_color="#E5E7EB")
            pb.pack(side="left", fill="x", expand=True, padx=8)
            pb.set(prog)
            ctk.CTkLabel(f, text=val, font=ctk.CTkFont(size=11, weight="bold"), text_color=col if "left" in val else "#000").pack(side="right")