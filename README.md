
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

```bash
python -m venv venv
source venv/bin/activate  # Linux
venv\Scripts\activate     # Windows
```

```bash
pip install -r requirements.txt
```

Crie um `.env`:

```env
SECRET_KEY=sua-chave
DEBUG=True
GEMINI_API_KEY=sua-chave
```

```bash
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

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

👉 Projeto ideal para portfólio backend Django



