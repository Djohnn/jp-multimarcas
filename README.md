
<p align="center">
  🌎 Language:
  <a href="#portugues">🇧🇷 PT-BR</a> |
  <a href="#english">🇺🇸 EN</a>
</p>

---

<a id="portugues"></a>
# 🚗 JP Multimarcas — Sistema de Gestão de Veículos

![Django](https://img.shields.io/badge/Django-6.0-green)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-Database-blue)
![Deploy](https://img.shields.io/badge/Deploy-Production-success)
![Status](https://img.shields.io/badge/Status-Online-brightgreen)

Sistema web completo para gestão de veículos (carros e motos), com CRM de leads, autenticação e automação com IA.

👉 **Projeto real em produção com Nginx + Gunicorn + HTTPS + Cloudflare**

---

## 🌐 Acesse o Projeto

🔗 https://djohnn.dev

---

## 📌 Sobre o Projeto

O **JP Multimarcas** é um sistema ERP desenvolvido com Django para revendas de veículos, com foco em:

- gestão de estoque
- automação de vendas
- captação de leads
- aumento de conversão

O projeto evoluiu além do CRUD básico, incorporando **segurança, automação e deploy real em produção**.

---

## ⚙️ Funcionalidades

- 🏎️ Cadastro completo de carros e motos  
- 📊 Controle de estoque automático  
- 🤖 Geração de descrição com IA (Google Gemini)  
- 📈 CRM de Leads com pipeline de vendas  
- 🔐 Controle de acesso por usuário (Ownership)  
- 💬 Integração com WhatsApp  

---

## 🧠 Diferenciais Técnicos

- Arquitetura modular com Django Apps
- Class-Based Views (CBVs)
- Uso de Mixins para segurança e reuso
- Django Signals para automação
- Integração com API externa (IA)
- Sistema preparado para evolução SaaS

---

## 🔐 Segurança

O sistema implementa isolamento de dados por usuário:

- `OwnerRequiredMixin`
- `OwnerQuerySetMixin`
- `UserFormKwargsMixin`

👉 Garante que cada usuário acessa apenas seus próprios dados

---

## 🤖 Automação com IA

Utiliza **Google Gemini API** para gerar descrições automaticamente:

- `pre_save` → gera descrição inteligente  
- `post_save` → atualiza estoque  
- `post_delete` → sincroniza inventário  

---

## 🏗️ Arquitetura

```bash
apps/
├── account/
├── cars/
├── motorcycle/
├── leads/
````

Estrutura modular para facilitar manutenção e escalabilidade.

---

## 🚀 Deploy em Produção

O projeto foi implantado manualmente em servidor Linux utilizando:

* **Gunicorn**
* **Nginx**
* **PostgreSQL**
* **Cloudflare (HTTPS + proteção)**

### Infraestrutura:

* VPS Linux (Ubuntu)
* Configuração de domínio real
* HTTPS com Let's Encrypt
* Firewall (UFW)
* Variáveis seguras com `.env`

---

## 🛠️ Tecnologias

* Python
* Django
* PostgreSQL
* HTML / CSS / JS
* Google Gemini API
* Nginx + Gunicorn

---

## ▶️ Como rodar localmente

```bash
git clone https://github.com/SEU-USUARIO/jp-multimarcas.git
cd jp-multimarcas
```
2. Crie e ative o ambiente virtual
```bash
python -m venv venv
```

No Linux/Mac:
```bash
source venv/bin/activate      
```

No Windows:
```bash
venv\Scripts\activate  
```

3. Instale as dependências
```bash
pip install -r requirements.txt
```

Crie um `.env` na raiz do projeto com as variáveis necessárias.:
Exemplo:
```env
SECRET_KEY=sua-chave
DEBUG=True
GEMINI_API_KEY=sua-chave
ALLOWED_HOSTS=127.0.0.1,localhost
DATABASE_NAME=nome_do_banco
DATABASE_USER=usuario
DATABASE_PASSWORD=senha
DATABASE_HOST=localhost
DATABASE_PORT=5432
```

Banco de dados
Executar migrações
```bash
python manage.py makemigrations
python manage.py migrate
```

Criar superusuário

```bash
python manage.py createsuperuser
```

Como rodar o projeto
```bash
python manage.py runserver
```

Acesse em:
```bash
http://127.0.0.1:8000/
```

---

# 🔐 Permissões e Autenticação

O sistema utiliza autenticação padrão do Django com controle de acesso por propriedade dos dados.

* ✔️ Usuários autenticados podem acessar o sistema
* 🔒 Cada usuário só pode **editar e excluir seus próprios registros**
* 🚫 Tentativas de acesso a registros de terceiros retornam **404 (não encontrado)**
* 🛡️ Validações aplicadas em múltiplas camadas:

  * Views (mixins de autorização)
  * Forms (validação de instância)
  * Templates (controle visual)
* ⚙️ Utiliza o sistema nativo de autenticação do Django (`User`)

### 📄 Paginação (Paginator)

A listagem de leads utiliza paginação nativa do Django para melhorar a performance e organização dos dados exibidos.

- Implementada através da propriedade `paginate_by` na `ListView`
- Limita a exibição para **20 leads por página**
- Evita sobrecarga de dados em páginas com grande volume de registros
- Melhora a experiência do usuário na navegação

#### ⚙️ Implementação

```python
class LeadListView(ListView):
    model = Lead
    template_name = 'leads/lead_list.html'
    context_object_name = 'leads'
    paginate_by = 20
````

#### 🔗 Navegação

O Django gerencia automaticamente:

* `page_obj` → objeto da página atual
* `is_paginated` → indica se há paginação
* `paginator` → controle total das páginas

Exemplo de uso no template:

```html
{% if is_paginated %}
  {% if page_obj.has_previous %}
    <a href="?page={{ page_obj.previous_page_number }}">Anterior</a>
  {% endif %}

  <span>Página {{ page_obj.number }} de {{ page_obj.paginator.num_pages }}</span>

  {% if page_obj.has_next %}
    <a href="?page={{ page_obj.next_page_number }}">Próxima</a>
  {% endif %}
{% endif %}
```

# 🌐 Endpoints / Rotas Principais

## 🔑 Autenticação

```bash
/login/        # Login do usuário
/logout/       # Logout
```

---

## 🏠 Página Inicial

```bash
/              # Home com listagem de carros e motos
```

* Filtros por preço (`sale_price`)
* Exibição dinâmica de veículos disponíveis

---

## 🚗 Carros

```bash
/cars/                    # Listagem de carros
/cars/create/             # Cadastro de carro
/cars/<int:pk>/           # Detalhe do carro
/cars/<int:pk>/update/    # Atualização (somente dono)
/cars/<int:pk>/delete/    # Exclusão (somente dono)
```

### 🔒 Regras de acesso

* Apenas o dono pode:

  * editar (`update`)
  * excluir (`delete`)
* Outros usuários:

  * apenas visualizam o detalhe
  * veem o nome do criador do anúncio

---

## 🏍️ Motos

```bash
/motorcycle/                     # Listagem de motos
/motorcycle/create/             # Cadastro de moto
/motorcycle/<int:pk>/           # Detalhe da moto
/motorcycle/<int:pk>/update/    # Atualização (somente dono)
/motorcycle/<int:pk>/delete/    # Exclusão (somente dono)
```

### 🔒 Regras de acesso

* Mesma lógica aplicada aos carros:

  * controle por proprietário
  * proteção contra acesso indevido
  * validação no backend e frontend

---

## ⚙️ Administração

Painel administrativo Django:
```bash
/admin/    
```



## 📈 Leads (CRM)

### 🔐 Permissões e autenticação

O módulo de leads possui controle de acesso baseado no sistema de permissões do Django.

- A criação de leads é **pública**, feita através de formulários no site  
- Leads podem ser vinculados automaticamente ao usuário autenticado (quando houver)  
- A listagem de leads é **restrita a usuários staff** (`staff_member_required`)  
- A atualização de status também é **restrita a staff**  
- O sistema utiliza o modelo de permissões nativo do Django (`is_staff`)  

---

### 🔗 Endpoints / Rotas principais

- `/leads/` → Listagem de leads (restrito a staff, com paginação e filtro por status)  
- `/leads/new/` → Criação de lead (via formulário/modal no site)  
- `/leads/<int:pk>/status/` → Atualização de status do lead (restrito a staff)  

---

### ⚙️ Funcionalidades do módulo

- Captura de leads vinculados a **carros ou motos**  
- Validação para garantir que apenas um tipo de veículo seja selecionado  
- Redirecionamento automático para **WhatsApp** após criação do lead  
- Sistema de funil de vendas com status:
  - Novo  
  - Contatado  
  - Em negociação  
  - Fechado  
  - Perdido  
- Paginação na listagem (`20 leads por página`)  
- Filtro por status via query params (`?status=`)  
- Estatísticas no painel (total e por status)  

---

### 📲 Fluxo do Lead

```text
Cliente clica em "Tenho interesse"
→ Preenche formulário (nome, telefone, mensagem)
→ Lead é salvo no banco
→ Redirecionamento automático para WhatsApp com mensagem personalizada
````

---

### 🧠 Regras de validação

* Não é permitido selecionar **carro e moto ao mesmo tempo**
* É obrigatório selecionar **um veículo**
* Validação de existência do veículo no banco
* Atribuição automática de responsável (`assigned_to`) quando usuário autenticado

---

### 🔄 Integração com WhatsApp

Após a criação do lead, o sistema gera automaticamente uma mensagem com:

* Nome do cliente
* Veículo de interesse
* Ano do veículo
* Preço

E redireciona para:

```
https://wa.me/<numero>?text=<mensagem>
```

---

### 🗂️ Organização

* `LeadListView` → listagem com filtro e estatísticas
* `LeadCreateView` → criação + integração com WhatsApp
* `LeadUpdateStatusView` → atualização de status
* `LeadForm` → validações de negócio
* `LeadStatusForm` → atualização de status e responsável
* `Lead` → modelo principal com funil de vendas

---


* Gerenciamento completo de:

  * usuários
  * carros
  * motos
  * marcas
  * leads

---

# 🧠 Arquitetura de Segurança

O projeto aplica um padrão de segurança reutilizável:

* `OwnerRequiredMixin` → valida se o usuário é dono
* `OwnerQuerySetMixin` → filtra dados por usuário
* `UserFormKwargsMixin` → injeta usuário nos formulários

👉 Isso garante isolamento total de dados entre usuários (multiusuário seguro)

---

# 🚀 Diferencial do Projeto

* ✔️ Controle de acesso por proprietário (estilo SaaS)
* ✔️ Proteção contra acesso direto por URL
* ✔️ Testes automatizados validando segurança
* ✔️ Integração com IA (geração de descrição de veículos)
* ✔️ Estrutura escalável para múltiplos apps (cars e motorcycle)

---



---

## 📈 Próximas Evoluções

* [ ] Multi-tenant (SaaS)
* [ ] Dashboard com gráficos
* [ ] Integração com pagamento
* [ ] Sistema de notificações
* [ ] API REST (DRF)

---

## 👨‍💻 Autor

**John Oliveira**

Desenvolvedor focado em backend com Django, automação e sistemas web escaláveis.

---

## ⭐ Destaque

Este projeto demonstra:

* deploy real em produção
* resolução de problemas reais (403, 500, 502, upload, segurança)
* arquitetura limpa e escalável
* integração com IA

---

<a id="english"></a>
# 🇺🇸 English Version

---

# 🚗 JP Multimarcas — Vehicle Management System

![Django](https://img.shields.io/badge/Django-6.0-green)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-Database-blue)
![Deploy](https://img.shields.io/badge/Deploy-Production-success)
![Status](https://img.shields.io/badge/Status-Online-brightgreen)

A complete web system for vehicle management (cars and motorcycles), including lead CRM, authentication, and AI-powered automation.

👉 **Real project running in production with Nginx + Gunicorn + HTTPS + Cloudflare**

---

## 🌐 Access the Project

🔗 https://djohnn.dev

---

## 📌 About the Project

**JP Multimarcas** is an ERP system built with Django for vehicle dealerships, focused on:

- inventory management  
- sales automation  
- lead generation  
- conversion optimization  

This project goes beyond a basic CRUD, incorporating **security, automation, and real production deployment**.

---

## ⚙️ Features

- 🏎️ Full car and motorcycle management  
- 📊 Automatic inventory control  
- 🤖 AI-generated vehicle descriptions (Google Gemini)  
- 📈 Lead CRM with sales pipeline  
- 🔐 User-based access control (ownership)  
- 💬 WhatsApp integration  

---

## 🧠 Technical Highlights

- Modular architecture with Django apps  
- Class-Based Views (CBVs)  
- Mixins for security and reusability  
- Django Signals for automation  
- External API integration (AI)  
- SaaS-ready system design  

---

## 🔐 Security

The system enforces user-level data isolation:

- `OwnerRequiredMixin`  
- `OwnerQuerySetMixin`  
- `UserFormKwargsMixin`  

👉 Ensures each user can only access their own data

---

## 🤖 AI Automation

Uses **Google Gemini API** to automatically generate descriptions:

- `pre_save` → generates smart description  
- `post_save` → updates inventory  
- `post_delete` → syncs inventory  

---

## 🏗️ Architecture

```bash
apps/
├── account/
├── cars/
├── motorcycle/
├── leads/
````

Modular structure designed for scalability and maintainability.

---

## 🚀 Production Deployment

The project was manually deployed on a Linux server using:

* **Gunicorn**
* **Nginx**
* **PostgreSQL**
* **Cloudflare (HTTPS + protection)**

### Infrastructure:

* Linux VPS (Ubuntu)
* Custom domain configuration
* HTTPS with Let's Encrypt
* Firewall (UFW)
* Environment variables via `.env`

---

## 🛠️ Technologies

* Python
* Django
* PostgreSQL
* HTML / CSS / JavaScript
* Google Gemini API
* Nginx + Gunicorn

---

## ▶️ Running Locally

```bash
git clone https://github.com/YOUR-USERNAME/jp-multimarcas.git
cd jp-multimarcas
```

2. Create and activate virtual environment

```bash
python -m venv venv
```

Linux/Mac:

```bash
source venv/bin/activate
```

Windows:

```bash
venv\Scripts\activate
```

3. Install dependencies

```bash
pip install -r requirements.txt
```

Create a `.env` file:

```env
SECRET_KEY=your-key
DEBUG=True
GEMINI_API_KEY=your-key
ALLOWED_HOSTS=127.0.0.1,localhost
DATABASE_NAME=db_name
DATABASE_USER=user
DATABASE_PASSWORD=password
DATABASE_HOST=localhost
DATABASE_PORT=5432
```

Run migrations:

```bash
python manage.py makemigrations
python manage.py migrate
```

Create superuser:

```bash
python manage.py createsuperuser
```

Run server:

```bash
python manage.py runserver
```

Access:

```bash
http://127.0.0.1:8000/
```

---

# 🔐 Permissions and Authentication

The system uses Django's authentication with ownership-based access control.

* ✔️ Authenticated users can access the system
* 🔒 Users can **only edit and delete their own records**
* 🚫 Unauthorized access returns **404 (not found)**
* 🛡️ Validation layers:

  * Views (authorization mixins)
  * Forms (instance validation)
  * Templates (UI restrictions)
* ⚙️ Uses Django's built-in `User` model

---

### 📄 Pagination

Lead listing uses Django’s built-in pagination to improve performance and usability.

* Implemented via `paginate_by` in `ListView`
* Limits results to **20 leads per page**
* Prevents overload with large datasets
* Improves navigation experience

---

# 🌐 Main Endpoints

## 🔑 Authentication

```
/login/
/logout/
```

---

## 🏠 Home

```
/
```

* Filters by price
* Dynamic vehicle display

---

## 🚗 Cars

```
/cars/
/cars/create/
/cars/<int:pk>/
/cars/<int:pk>/update/
/cars/<int:pk>/delete/
```

Access rules:

* Only owner can edit/delete
* Others can only view

---

## 🏍️ Motorcycles

```
/motorcycle/
/motorcycle/create/
/motorcycle/<int:pk>/
/motorcycle/<int:pk>/update/
/motorcycle/<int:pk>/delete/
```

Same ownership rules as cars.

---

## ⚙️ Admin

```
/admin/
```

---

## 📈 Leads (CRM)

### 🔐 Permissions

* Lead creation is **public**
* Lead management is **staff-only**
* Uses Django `is_staff`

---

### 🔗 Endpoints

```
/leads/
/leads/new/
/leads/<int:pk>/status/
```

---

### ⚙️ Features

* Linked to car or motorcycle
* Validation rules
* WhatsApp redirect
* Sales pipeline
* Filtering and pagination

---

### 📲 Lead Flow

```
User clicks "Interested"
→ fills form
→ lead saved
→ redirected to WhatsApp
```

---

### 🧠 Validation Rules

* Cannot select both car and motorcycle
* Must select one
* Validates existence in DB
* Auto assigns user if authenticated

---

### 🔄 WhatsApp Integration

Redirects to:

```
https://wa.me/<number>?text=<message>
```

---

## 🧠 Security Architecture

Reusable security pattern:

* `OwnerRequiredMixin`
* `OwnerQuerySetMixin`
* `UserFormKwargsMixin`

---

## 🚀 Project Highlights

* ✔️ Ownership-based access control
* ✔️ URL protection
* ✔️ Automated tests (security)
* ✔️ AI integration
* ✔️ Scalable structure

---

## 📈 Future Improvements

* SaaS multi-tenant
* Analytics dashboard
* Payment integration
* Notifications
* REST API (DRF)

---

## 👨‍💻 Author

**John Oliveira**

Backend developer focused on Django, automation, and scalable web systems.

---

## ⭐ Highlights

This project demonstrates:

* real production deployment
* solving real-world issues (403, 500, 502, uploads, security)
* clean and scalable architecture
* AI integration




