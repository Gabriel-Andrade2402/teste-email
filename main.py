import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

remetente = 'gabriel.andrade2402@gmail.com'
senha = 'vier nrxy jfje bskq'
destinatario = 'pedrinhosoares5859@gmail.com'

# Criando o e-mail
mensagem = MIMEMultipart('alternative')
mensagem['Subject'] = 'Teste de Email HTML'
mensagem['From'] = remetente
mensagem['To'] = destinatario

# Conteúdo em HTML
html = """
<!DOCTYPE html>
<html lang="pt-BR">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width">
  <style>
    @media only screen and (max-width: 600px) {
      .stack-column {
        display: block !important;
        width: 100% !important;
        max-width: 100% !important;
      }
      .text-center {
        text-align: center !important;
      }
      .highlight {
        font-size: 20px !important;
      }
    }
  </style>
</head>
<body style="margin:0; padding:0; font-family:Arial, sans-serif;">
    <table role="presentation" border="0" cellpadding="0" cellspacing="0" width="100%" style="border-collapse: collapse;">
        <tr>
            <!-- Coluna 1: Duas linhas de texto -->
            <td class="stack-column" style="width:66.66%; padding:10px;" valign="top">
                <img src="https://img.freepik.com/psd-gratuitas/ilustracao-de-codigo-de-barras-isolada_23-2150584084.jpg?t=st=1747764035~exp=1747767635~hmac=3f20000d1f061d28d812ed61ae503e8333dde5e090d20bd5e6fbdd0ebb0f1819&w=826" alt="Logomarca" 
                style="max-width:50%; display:block;">
            </td>
            <td class="stack-column" style="width:66.66%; padding:10px;" valign="top">
                <img src="https://img.freepik.com/vetores-gratis/escaneie-me-o-codigo-qr_78370-2915.jpg?t=st=1747763971~exp=1747767571~hmac=18cbe2d7f6ad0a3532066013a5f68c19c3e6a73abcb11e7426178d37cb063f80&w=826" alt="Logomarca" 
                style="max-width:50%; display:block;">
            </td>
        </tr>
    </table>
    <!-- LINHA 1: 3 colunas (2/12, 6/12, 4/12) -->
    <table role="presentation" border="0" cellpadding="0" cellspacing="0" width="100%" style="border-collapse: collapse;">
        <tr>
            <!-- Coluna 1: Logomarca -->
            <td class="stack-column" style="width:16.66%; padding:10px; border:1px solid #000;" valign="top">
                <img src="https://brasao.org/wp-content/uploads/2018/08/brasao-estado-de-sao-paulo.png" alt="Logomarca" style="max-width:100%; display:block;">
            </td>
            <!-- Coluna 2: Texto com 3 linhas -->
            <td class="stack-column" style="width:50%; padding:10px; border:1px solid #000;" valign="top">
                <p style="margin:0 0 5px;">Governo do Estado de São Paulo</p>
                <p style="margin:0 0 5px;">Secretaria da Fazenda e Planejamento</p>
                <p style="margin:0;">Documento de Arrecadação de Receitas Estaduais</p>
            </td>
            <!-- Coluna 3: Imagem + Texto -->
            <td class="stack-column" style="width:33.33%; padding:10px; border:1px solid #000;" valign="top">
                <img src="https://www.pagamentos.fazenda.sp.gov.br/Pagamentos/WebSite/App_Themes/Default/Images/Daresp.png" alt="Imagem" style="max-width:100%; display:block; margin-bottom:5px;">
                <p style="margin:0;">Documento Principal</p>
            </td>
        </tr>
    </table>

    <!-- LINHA 2: 2 colunas (8/12, 4/12) -->
    <table role="presentation" border="0" cellpadding="0" cellspacing="0" width="100%" style="border-collapse: collapse;">
        <tr>
            <!-- Coluna 1: Duas linhas de texto -->
            <td class="stack-column" style="width:66.66%; padding:10px; border:1px solid #000;" valign="top">
                <p style="margin:0 0 5px;">01 - Nome / Razão Social</p>
                <p style="margin:0;">Contribuinte</p>
            </td>
            <!-- Coluna 2: Duas linhas de texto alinhadas -->
            <td class="stack-column" style="width:33.33%; padding:10px; border:1px solid #000;" valign="top">
                <div style="display: flex; flex-direction: column; height: 100%;">
                    <div style="text-align: left;">07 - Data de Vencimento</div>
                    <div style="margin-top: auto; text-align: right;">31/07/2021</div>
                </div>
            </td>
        </tr>
    </table>

    <!-- LINHA 3: Estrutura semelhante à LINHA 2 -->
    <table role="presentation" border="0" cellpadding="0" cellspacing="0" width="100%" style="border-collapse: collapse;">
        <tr>
            <!-- Coluna 1: Duas linhas de texto -->
            <td class="stack-column" style="width:66.66%; padding:10px; border:1px solid #000;" valign="top">
                <p style="margin:0 0 5px;">02 - Endereço</p>
                <p style="margin:0;">Endereço do contribuinte, 999 São Paulo</p>
            </td>
            <!-- Coluna 2: Duas linhas de texto alinhadas -->
            <td class="stack-column" style="width:33.33%; padding:10px; border:1px solid #000;" valign="top">
                <div style="display: flex; flex-direction: column; height: 100%;">
                    <div style="text-align: left;">08 - Valor Total</div>
                    <div style="margin-top: auto; text-align: right;">R$ 400.000,00</div>
                </div>
            </td>
        </tr>
    </table>

    <!-- LINHA 4: 2 colunas (8/12, 4/12) -->
    <table role="presentation" border="0" cellpadding="0" cellspacing="0" width="100%" style="border-collapse: collapse;">
        <tr>
            <!-- Coluna 1: Duas linhas -->
            <td class="stack-column" style="width:66.66%; border:1px solid #000;" valign="top">
                <!-- Linha 1: 3 colunas com duas linhas de texto cada -->
                <table role="presentation" border="0" cellpadding="0" cellspacing="9" width="100%">
                    <tr>
                    <td style="width:33.33%; padding:5px;">
                        <p style="margin:0 0 5px;">03 - CNPJ Base / CPF</p>
                        <p style="margin:0;">99.999.999</p>
                    </td>
                    <td style="width:33.33%; padding:5px;">
                        <p style="margin:0 0 5px;">04 - Telefone</p>
                        <p style="margin:0;">(11)99999-9999</p>
                    </td>
                    <td style="width:33.33%; padding:5px;">
                        <p style="margin:0 0 5px;">05 - Quantidade de Documentos Detalhe</p>
                        <p style="margin:0;">1</p>
                    </td>
                    </tr>
                </table>
                <!-- Linha 2: Texto -->
                <p style="margin:10px 0 0; padding:10px; border-top: 2px solid #000;">06 - Observações</p>
            </td>
            <!-- Coluna 2: 3 linhas de texto, com destaque no texto do meio -->
            <td class="stack-column" style="width:33.33%; padding:10px; border:1px solid #000; text-align:center;" valign="middle">
                <p style="margin:0;">09 - Número do DARE</p>
                <p class="highlight" style="margin:10px 0; font-size:18px; font-weight:bold;">9999999999999999</p>
                <p style="margin:0;">Emissão: 01/07/2021</p>
            </td>
        </tr>
    </table>
    <table role="presentation" border="0" cellpadding="0" cellspacing="0" width="100%" style="border-collapse: collapse;">
        <tr>
            <!-- Coluna 1: Duas linhas de texto -->
            <td class="stack-column" style="width:66.66%; padding:10px; border-right:1px solid #000;" valign="top">
                <p style="margin:0 0 5px;">10 - Autenticação Mecânica</p>
            </td>
            <td class="stack-column" style="width:66.66%; padding:10px; border-left:1px solid #000;" valign="top">
                <p style="margin:0 0 5px;">Via do Banco</p>
            </td>
        </tr>
    </table>
</body>
</html>
"""

# Anexando o conteúdo HTML
parte_html = MIMEText(html, 'html')
mensagem.attach(parte_html)

# Enviando o e-mail via SMTP (Gmail neste caso)
try:
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as servidor:
        servidor.login(remetente, senha)
        servidor.sendmail(remetente, destinatario, mensagem.as_string())
    print("Email enviado com sucesso!")
except Exception as e:
    print(f"Erro ao enviar e-mail: {e}")
