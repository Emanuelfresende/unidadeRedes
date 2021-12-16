# http-tupi:  _HTTP-simple_

## _Emanuel Freitas Resende_

 [HTTP](https://developer.mozilla.org/pt-BR/docs/Web/HTTP/Overview) é um protocolo que permite a obtenção de recursos na web. É um protocolo extensível com uso do  cabeçalho ( _headers_) para inclusão de novos campos e valores.  A especificação das mensagens HTTP e extensões estão definidas na [RFC 7230](https://datatracker.ietf.org/doc/html/rfc7230). Nesta RFC são definidos os conceitos de proxy, gateway e túneis HTTP como agentes intermediários capazes de interpretar campos de mensagens de cliente e servidor e em alguns casos traduzir para outros formatos não padronizados pelo HTTP ou redirecionar para servidores internos. Atualmente existe um [grupo de trabalho na Internet](https://httpwg.org/specs/) pesquisando novas extensões para o HTTP. 
 
__Proponha__ uma nova aplicação para resolver um problema específico de um usuário na web. Defina uma nova extensão para o HTTP denominada HTTP Tupi com a inclusão de novos campos de cabeçalho. __Implemente o cliente e servidor HTTP Tupi__, para sua solução proposta. O servidor HTTP Tupi deve ser capaz de reconhecer uma mensagem HTTP Tupi e realizar ações, incluindo a reposta com conteúdo diferente do HTTP/1.1. As respostas podem incluir dados em outros formatos diferentes do HTML, como XML e JSON, por exemplo, de acordo com a especificação de sua proposta.

Se seu servidor receber mensagens sem a extensão do campo proposto, o servidor deve agir de acordo com o protocolo HTTP/1.1. Se a mensagem originada do cliente incluir a extensão no cabeçalho, o servidor deve responder de acodo comm protocolo HTTP Tupi.

## Qual o problema considerado?  
_Justifique a aplicação de sua solução proposta_

> O problema considerado foi a busca de palavras dentro do site do Departamento de Relações Internacionais da Universidade Federal De Sergipe (UFS), onde o usuário informa o url do site e a quantidade de vezes que a palavra aparece, para considerar possiveis correções em seu site, através de uma requisição em http.
A aplicação baseada em uma variação do http, o HTTP/Tupi, retorna um formato text/plain de uma  página que o usuário informa pelo seu url. QUando protocolo HTTP/1.1 é chamado, ele retorna a resposta através do arquivo text/html. Caso solicitado pelo HTTP/Tupi, o servidor apontará a resposta da busca com conteudo text/plain.

## Qual o público alvo?  
_Descreva quais os usuários em potencial para sua aplicação web_

>Usuários com capacidade técnica para entender e desenvolver qualquer mudança necessária, e dar suporte para pesquisa aos que tiverem necessidade.

## Qual a arquitetura?  
_Descreva quais os módulos de hardware, software e protocolos necessários para sua aplicação, restringindo-se às características dos protocolos da camada de aplicação_

> Hardware em uma máquina virtual no laboratório Elan da UFS. O software utilizado foi dentro do linux, com python 3.7. Os protocolos utilizados foram: TCP e HTTP. As bibliotecas foram:
socket,string,datetime,os,BeautifulSoup,requests e re.

## Qual o formato do protocolo?
_Especifique o que um programador precisa saber para implementar seu protocolo em qualquer linguagem_

> Primeiro deverá saber a base do sistema que vai utilizar. Deverá estudar a linguagem de programação, neste caso python, e ter domínio das bibliotecas utilizadas.
Depois ele irá estudar como o protocolo HTTP funciona as conexões entre servidor e cliente. A conexão será atraves de uma conexão TCP, e as requisições em e mensagens em HTTP.
O protocolo é formatado entre method, path,version e headers.

### Como as mensagens são definidas?
_Especifique mensagens enviadas pelo cliente e respostas do servidor_

> O cliente envia mensagens de requisição para identificar parágrafos que contém a palavra solicitada. A mensagem é encapsulada e traduzida pelo servidor, que apresenta as resposta para o usuário.

### Quais os campos definidos?
_campos devem seguir padrão NOME_DO_CAMPO: VALORES_ 

> DATE: %a, %d %b %Y %H:%M:%S %Z

> SERVER: SERVER

> CONTENT-TYPE: TEXT/HTML

> HOST: UFS.CLIENT.BR

> ACCEPT-LANGUAGE: *

> URL-FIELD: <URL>

### Quais os possíveis valores de cada campo?
apresentado em detalhes acima


## Como a aplicação pode ser testada no Core?

_Descreva como o servidor pode ser implantado e testado, apresentando um manual de uso_ 
> Uma aplicação simples, os arquivos TCPserver.py e TCPclient.py são adicionados, sendo executados em suas redes com o comando python3. QUando a conexão se inicia, o cliente faz as solicitações do url do departamento, ou caso queira, qualquer outro link, e escolher a palavra que quer fazer a busca. O servidor encontrará e imprimirá a resposta em tela.

## Faça um registro do funcionamento de sua aplicação 
_Apresente um exemplo de teste mostrando que o cliente e o servior  HTTP Tupi funcionou corretamente_
- A atividade é apresentada no link https://github.com/Emanuelfresende/unidadeRedes/blob/main/aplicacaoTCP.pdf, com o arquivo aplicacaoTCP.pdf que vai demostrar o passo a passo da execução da atividade.
