import customtkinter as ctk

class PedidosView(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent, fg_color="#FFFFFF", corner_radius=15)
        
        ctk.CTkLabel(self, text="GERENCIAMENTO DE PEDIDOS 📝", font=ctk.CTkFont(size=18, weight="bold"), text_color="#3A1A10").pack(anchor="w", padx=20, pady=15)

        # Tabela simplificada de pedidos
        scroll = ctk.CTkScrollableFrame(self, fg_color="transparent")
        scroll.pack(fill="both", expand=True, padx=15, pady=(0, 15))

        headers = ["ID", "Cliente", "Itens", "Total", "Status", "Ação"]
        h_frame = ctk.CTkFrame(scroll, fg_color="#F3EBE1", height=30)
        h_frame.pack(fill="x", pady=2)
        for h in headers:
            ctk.CTkLabel(h_frame, text=h, font=ctk.CTkFont(size=12, weight="bold"), text_color="#000", width=120).pack(side="left", expand=True)

        # Exemplo de pedidos
        pedidos = [
            ("#101", "Carlos Silva", "2x Super Catatau", "R$ 64,00", "Em Preparo"),
            ("#102", "Ana Souza", "1x Cheddar Bacon", "R$ 28,00", "Pronto"),
            ("#103", "João Pedro", "1x Batata + 1x Cerveja", "R$ 32,00", "Entregue")
        ]

        for p in pedidos:
            row = ctk.CTkFrame(scroll, fg_color="#F9F9F9", height=35)
            row.pack(fill="x", pady=2)
            for val in p:
                ctk.CTkLabel(row, text=val, font=ctk.CTkFont(size=12), text_color="#000", width=120).pack(side="left", expand=True)
            ctk.CTkButton(row, text="Detalhes", width=80, height=24, fg_color="#3A1A10", font=ctk.CTkFont(size=11)).pack(side="left", expand=True)