# 🚗 JP Multimarcas — Sistema de Gestão de Veículos

Sistema web completo para gestão de estoque de veículos (carros e motos), com CRM de leads, autenticação de usuários e integração com IA para geração automática de descrições.

---

## 📌 Visão Geral

O **JP Multimarcas** é um ERP web desenvolvido com Django, focado em revendas de veículos. O sistema permite uma gestão centralizada e automatizada do negócio.

### Principais Funcionalidades:
- 🏎️ **Gestão de Estoque:** Cadastro e gerenciamento completo de carros e motos.
- 📊 **Controle Automático:** Atualização de inventário em tempo real.
- 🤖 **IA com Google Gemini:** Geração de descrições comerciais automáticas.
- 📈 **CRM de Leads:** Captação e gestão de clientes interessados.
- 🔐 **Segurança:** Controle de acesso robusto por usuário (Ownership).
- 💬 **Conversão:** Integração direta com WhatsApp para fechamento de vendas.

---

## 🏗️ Arquitetura do Projeto

A estrutura do projeto segue o padrão modular do Django para facilitar a manutenção e escalabilidade:

```text
jp-multimarcas/
├── app/
│   ├── __init__.py
│   ├── asgi.py
│   ├── mixins.py
│   ├── settings.py
│   ├── urls.py
│   ├── views.py
│   └── wsgi.py
├── apps/
│   ├── account/
│   │   ├── migrations/
│   │   ├── __init__.py
│   │   ├── admin.py
│   │   ├── apps.py
│   │   ├── models.py
│   │   ├── tests.py
│   │   ├── urls.py
│   │   └── views.py
│   ├── cars/
│   │   ├── migrations/
│   │   ├── templatetags/
│   │   ├── __init__.py
│   │   ├── admin.py
│   │   ├── apps.py
│   │   ├── forms.py
│   │   ├── models.py
│   │   ├── signals.py
│   │   ├── tests.py
│   │   ├── urls.py
│   │   └── views.py
│   ├── leads/
│   │   ├── migrations/
│   │   ├── __init__.py
│   │   ├── admin.py
│   │   ├── apps.py
│   │   ├── forms.py
│   │   ├── models.py
│   │   ├── tests.py
│   │   ├── urls.py
│   │   └── views.py
│   └── motorcycle/
│       ├── migrations/
│       ├── __init__.py
│       ├── admin.py
│       ├── apps.py
│       ├── forms.py
│       ├── models.py
│       ├── signals.py
│       ├── tests.py
│       ├── urls.py
│       └── views.py
├── gemini_api/
│   └── client.py
├── media/
│   ├── cars/
│   └── motorcycle/
├── static/
│   ├── css/
│   │   ├── account/
│   │   │   └── auth.css
│   │   ├── cars/
│   │   │   ├── car_delete.css
│   │   │   ├── car_detail.css
│   │   │   ├── car.css
│   │   │   └── new_car.css
│   │   ├── components/
│   │   │   ├── footer.css
│   │   │   └── navbar.css
│   │   ├── leads/
│   │   │   └── lead_list.css
│   │   ├── motorcycle/
│   │   │   ├── motorcycle_delete.css
│   │   │   ├── motorcycle_detail.css
│   │   │   ├── motorcycle.css
│   │   │   └── new_motorcycle.css
│   │   ├── base.css
│   │   └── home.css
│   ├── img/
│   │   └── logo.png
│   └── js/
│       ├── home.js
│       ├── leads.js
│       ├── navbar.js
│       ├── new_car.js
│       └── new_motorcycle.js
├── templates/
│   ├── account/
│   │   ├── login.html
│   │   └── register.html
│   ├── cars/
│   │   ├── car_delete.html
│   │   ├── car_detail.html
│   │   ├── car_update.html
│   │   ├── cars.html
│   │   ├── new_brand.html
│   │   └── new_car.html
│   ├── leads/
│   │   ├── lead_list.html
│   │   └── lead_status_form.html
│   ├── motorcycle/
│   │   ├── brand_form.html
│   │   ├── motorcycle_confirm_delete.html
│   │   ├── motorcycle_detail.html
│   │   ├── motorcycle_form.html
│   │   ├── motorcycle_list.html
│   │   └── motorcycle_update.html
│   ├── partials/
│   │   ├── footer.html
│   │   └── navbar.html
│   ├── base.html
│   └── home.html
├── .env
├── .gitignore
├── estrutura.txt
├── manage.py
├── README.md
└── requirements.txt
```

---

## ⚙️ Tecnologias Utilizadas

- **Backend:** Django 6
- **Banco de Dados:** PostgreSQL
- **Frontend:** HTML5, CSS3 (Variáveis Globais), JavaScript
- **IA:** Google Gemini API
- **Configuração:** `python-decouple`
- **Deploy:** Railway

---

## 🔐 Segurança e Permissões

O sistema implementa uma camada de segurança baseada em **Ownership** (Propriedade), garantindo que um usuário acesse apenas seus próprios dados.

| Mixin | Função |
| :--- | :--- |
| `OwnerRequiredMixin` | Bloqueia acesso a objetos de terceiros. |
| `OwnerQuerySetMixin` | Filtra o banco de dados para exibir apenas o que pertence ao usuário logado. |
| `UserFormKwargsMixin` | Injeta o usuário logado nos formulários para validação de posse. |

---

## 🚘 Módulo de Carros

**Funcionalidades:**
- Cadastro técnico e comercial completo.
- Controle de preços: Compra, Venda e Tabela FIPE.
- Check-list de histórico: IPVA pago, sinistro, único dono.
- **Validações:** Preço mínimo de R$ 20.000 e ano mínimo 1980.

---

## 🏍️ Módulo de Motos

Desenvolvido com especificidades para o nicho de duas rodas:
- **Campos Específicos:** Cilindradas (cc) e tipo (Naked, Trail, Esportiva, etc).
- **Validações Adaptadas:** Preço mínimo de R$ 1.000.
- **IA Contextual:** Bio gerada considerando a categoria e potência da moto.

---

## 📈 Módulo de Leads (CRM)

Sistema de captura para transformar visitantes em clientes:
- **Captura:** O cliente demonstra interesse em um veículo.
- **Registro:** Nome e telefone são salvos no Pipeline de Vendas.
- **Conversão:** Redirecionamento instantâneo para o WhatsApp do vendedor.
- **Pipeline de Vendas:**
  - *Novo*
  - *Contatado*
  - *Em negociação*
  - *Fechado*
  - *Perdido*

**Fluxo de Captação:**
1. Cliente clica em "Tenho Interesse"
2. Preenche nome e telefone
3. Lead é salvo no sistema
4. Redirecionamento automático para o WhatsApp do vendedor

---

## 🤖 Integração com IA & Automação

O sistema utiliza a **Google Gemini API** para otimizar o tempo de cadastro. Através de **Django Signals**, o fluxo é automatizado:
- `pre_save`: Detecta se a descrição está vazia e solicita à IA um texto comercial otimizado.
- `post_save`: Atualiza os contadores do inventário global.
- `post_delete`: Sincroniza o estoque após a remoção de um item.

---

## 🚀 Como Executar o Projeto Localmente

Se você deseja testar o **JP Multimarcas** na sua máquina, siga o passo a passo abaixo. 

### 1. Pré-requisitos
Certifique-se de ter instalado em sua máquina:
- **Python** (versão 3.10 ou superior)
- **Git**
- Uma chave de API do **Google Gemini** (opcional, mas recomendada para testar a IA)

### 2. Clonar o Repositório
Abra o seu terminal e clone o projeto:

```bash
git clone [https://github.com/SEU-USUARIO/jp-multimarcas.git](https://github.com/SEU-USUARIO/jp-multimarcas.git)
cd jp-multimarcas
```

### 3. Criar e Ativar o Ambiente Virtual
É altamente recomendado usar um ambiente virtual para não misturar as dependências:

**No Windows:**
```bash
python -m venv venv
venv\Scripts\activate
```

**No Linux/Mac:**
```bash
python3 -m venv venv
source venv/bin/activate
```

### 4. Instalar as Dependências
Com o ambiente virtual ativado (você verá um `(venv)` no terminal), instale as bibliotecas necessárias:

```bash
pip install -r requirements.txt
```

### 5. Configurar Variáveis de Ambiente (.env)
O projeto utiliza a biblioteca `python-decouple` para proteger dados sensíveis. 
Na raiz do projeto (mesma pasta do `manage.py`), crie um arquivo chamado `.env` e adicione as seguintes linhas:

```ini
SECRET_KEY=sua-chave-secreta-do-django-aqui
DEBUG=True
GEMINI_API_KEY=sua-chave-api-do-google-gemini-aqui
```
*Nota: Para testar rapidamente, o sistema utilizará o banco de dados padrão SQLite (`db.sqlite3`).*

### 6. Executar as Migrações do Banco de Dados
Agora, vamos criar as tabelas no banco de dados para carros, motos, usuários e leads:

```bash
python manage.py migrate
```

### 7. Criar um Superusuário (Admin)
Para acessar o sistema e cadastrar os primeiros veículos, você precisa de um usuário administrador:

```bash
python manage.py createsuperuser
```
*(O terminal pedirá para você digitar um nome de usuário, e-mail e senha. A senha não aparece enquanto você digita, isso é normal do terminal).*

### 8. Rodar o Servidor
Tudo pronto! Agora é só ligar o servidor do Django:

```bash
python manage.py runserver
```

### 9. Acessar o Sistema
Abra o seu navegador e acesse:
👉 **http://localhost:8000**

Para testar a criação de veículos usando a integração com a IA, faça o login com o superusuário que você acabou de criar.

---

## 🚀 Próximas Evoluções
- [ ] Sistema Multi-tenant (SaaS) para múltiplas lojas.
- [ ] Dashboard analítico com gráficos de performance.
- [ ] Integração com gateways de pagamento.
- [ ] Fila de impressão para recibos e contratos.

---

## 👨‍💻 Autor
**John Oliveira** - Desenvolvedor Django focado em sistemas web robustos e automação inteligente.
```
