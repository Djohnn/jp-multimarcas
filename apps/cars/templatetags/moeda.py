from django import template

register = template.Library()

@register.filter(name='moeda_br')
def moeda_br(valor):
    try:
        valor = float(valor)
        # Formata: 30000.0 -> 30,000.00
        valor_formatado = f"{valor:,.2f}"
        
        # Troca para padrão brasileiro
        valor_formatado = valor_formatado.replace(",", "X") \
                                         .replace(".", ",") \
                                         .replace("X", ".")
        
        return f"R$ {valor_formatado}"
    except (ValueError, TypeError):
        return ""