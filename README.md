# Automação de Extração de Textos de TCC de Turismo

## Descrição do Projeto

Este projeto tem como objetivo automatizar a extração de textos de Trabalhos de Conclusão de Curso (TCCs) na área de Turismo, a partir de um site específico. O texto extraído será utilizado para a construção de um corpus linguístico, que servirá como base para o desenvolvimento de recursos pedagógicos.

## Funcionalidades

1. **Navegação e Download Automatizado de TCCs**: Utiliza o Selenium para navegar em um site específico e baixar arquivos PDF de TCCs.
2. **Extração de Texto de PDFs**: Utiliza a biblioteca PyPDF2 para extrair o texto dos arquivos PDF baixados.
3. **Armazenamento de Texto Extraído**: Os textos extraídos dos PDFs são combinados e salvos em um único arquivo de texto.

## Requisitos

- Python 3.6 ou superior
- Google Chrome
- ChromeDriver

## Bibliotecas Necessárias

Instale as bibliotecas necessárias utilizando o `pip`:

```sh
pip install selenium PyPDF2
```

## Estrutura do Projeto

```plaintext
.
├── extracao_tcc_turismo.py    # Script principal para extração e processamento
├── tccs/                      # Diretório onde os PDFs baixados são armazenados
├── tccs_extraidos/            # Diretório onde o arquivo de texto combinado é salvo
└── README.md                  # Documentação do projeto
```

## Configuração do Ambiente

1. **Google Chrome e ChromeDriver**: Certifique-se de que o Google Chrome está instalado em seu sistema. Baixe a versão correspondente do ChromeDriver [aqui](https://sites.google.com/a/chromium.org/chromedriver/downloads) e adicione o executável ao seu PATH do sistema.

2. **Estrutura de Diretórios**: Crie os diretórios `tccs` e `tccs_extraidos` no mesmo nível do script Python.

## Uso

1. **Configuração do Diretório de Download**: No script, ajuste a variável `destination_folder` para o caminho onde deseja salvar os PDFs baixados.
   
   ```python
   destination_folder = r"C:\Users\seu_usuario\caminho\para\tccs"
   ```

2. **Execução do Script**: Execute o script `extracao_tcc_turismo.py`:

   ```sh
   python extracao_tcc_turismo.py
   ```

3. **Resultado**: Após a execução, o arquivo de texto combinado será salvo no diretório `tccs_extraidos`.


## Considerações Finais

Este projeto é uma ferramenta útil para pesquisadores e educadores na área de Turismo, facilitando a coleta e análise de textos acadêmicos. Adapte as configurações e parâmetros conforme necessário para atender às suas necessidades específicas.