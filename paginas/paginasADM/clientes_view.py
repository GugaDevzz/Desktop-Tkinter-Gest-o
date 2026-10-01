import customtkinter as ctk

class ClientesView(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent, fg_color="#FFFFFF", corner_radius=15)
        
        ctk.CTkLabel(self, text="BASE DE CLIENTES 👥", font=ctk.CTkFont(size=18, weight="bold"), text_color="#3A1A10").pack(anchor="w", padx=20, pady=15)

        scroll = ctk.CTkScrollableFrame(self, fg_color="transparent")
        scroll.pack(fill="both", expand=True, padx=15, pady=(0, 15))

        clientes = [
            ("Mariana Costa", "(16) 99887-6655", "12 Pedidos", "VIP"),
            ("Lucas Mendes", "(16) 99112-3344", "5 Pedidos", "Regular"),
            ("Beatriz Lima", "(16) 98822-1100", "1 Pedido", "Novo")
        ]

        for nome, tel, compras, tag in clientes:
            row = ctk.CTkFrame(scroll, fg_color="#F9F9F9", height=40)
            row.pack(fill="x", pady=4, padx=5)
            ctk.CTkLabel(row, text=nome, font=ctk.CTkFont(size=13, weight="bold"), text_color="#000", width=180, anchor="w").pack(side="left", padx=15)
            ctk.CTkLabel(row, text=tel, font=ctk.CTkFont(size=12), text_color="#555", width=140).pack(side="left")
            ctk.CTkLabel(row, text=compras, font=ctk.CTkFont(size=12), text_color="#000", width=100).pack(side="left")
            ctk.CTkLabel(row, text=tag, font=ctk.CTkFont(size=11, weight="bold"), text_color="#3A1A10", width=80).pack(side="right", padx=15)