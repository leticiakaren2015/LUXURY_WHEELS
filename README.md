# Luxury_Wheels
Criando site de aluguel de carros

```mermaid
flowchart TD
 subgraph ADMIN["Dashboard Admin"]
    direction TB
        AD_RES["Nova Reserva"]
        AD_LIST_RES["Lista de Reserva"]
        AD_CLIENT["Lista de Cliente"]
        AD_VEH["Lista de Veículo"]
  end
 subgraph USER["Dashboard Usuário"]
    direction TB
        US_RES["Nova Reserva"]
  end
 subgraph LEG["Legenda"]
        LEG1(["Azul: Admin"])
        LEG2(["Verde: Usuário Normal"])
        LEG3(["Amarelo: Formulário / Criar"])
  end
    START(["Usuário acessa a Página Inicial"]) --> LOGIN["Fazer Login"] & REG["Registrar Usuário"]
    LOGIN --> AUTH{"Autenticação válida?"}
    AUTH -- Sim (admin) --> DASH_ADMIN["Dashboard Admin"]
    AUTH -- Sim (usuário) --> DASH_USER["Dashboard Usuário"]
    AUTH -- Não --> LOGIN
    REG --> SAVE_REG["Salvar Usuário"]
    SAVE_REG --> LOGIN
    DASH_ADMIN --> ADMIN & LOGOUT["Logout"]
    DASH_USER --> USER & LOGOUT
    AD_RES --> FORM_RES["Form: Cliente, Veículo, Data Início, Data Fim, Forma Pagamento, Valor Total"]
    FORM_RES --> CREATE_RES["Criar Reserva"]
    US_RES --> FORM_RES_U["Form: Cliente, Veículo, Data Início, Data Fim, Forma Pagamento, Valor Total"]
    FORM_RES_U --> CREATE_RES_U["Criar Reserva"]
    AD_LIST_RES --> LIST_RES["Lista: Cliente, Veículo, Data Início, Data Fim, Pagamento, Valor Total"]
    LIST_RES --> EDIT_RES["Editar Reserva"] & DEL_RES["Excluir Reserva"] & NEW_RES["Nova Reserva"]
    AD_CLIENT --> LIST_CLIENT["Lista: Nome, Email, Telefone, Categoria"]
    LIST_CLIENT --> EDIT_CLIENT["Editar Cliente"] & DEL_CLIENT["Excluir Cliente"] & NEW_CLIENT["Novo Cliente"]
    AD_VEH --> LIST_VEH["Lista: Marca, Modelo, Placa, Status"]
    LIST_VEH --> EDIT_VEH["Editar Veículo"] & DEL_VEH["Excluir Veículo"] & NEW_VEH["Novo Veículo"]
    LOGOUT --> START

    style LEG1 stroke:#000000,fill:#BBDEFB
    style LEG2 fill:#C8E6C9
    style LEG3 fill:#FFF9C4
    style ADMIN fill:#BBDEFB,stroke:#2b6cff,stroke-width:1px
    style USER fill:#C8E6C9,stroke:#2b8f4a,stroke-width:1px
    style FORM_RES fill:#fffacd,stroke:#b8860b
    style FORM_RES_U fill:#fffacd,stroke:#b8860b
    style LIST_RES fill:#BBDEFB,stroke:#2b6cff
    style LIST_CLIENT fill:#BBDEFB,stroke:#2b6cff
    style LIST_VEH fill:#BBDEFB,stroke:#2b6cff
    style LEG fill:#f5f5f5,stroke:#000000,stroke-width:1px
```
