## :page_facing_up: Descrição do Projeto

Esse repositório tem como objetivo entregar todas as pendências para o teste prático e detalhar o passo a passo para executar a aplicação.

## Instalação e execução da aplicação

### Ferramentas necessárias e suas versões

- Java version "13.0.2" 2020-01-14
- Gradle version 6.0.1
- Docker version 19.03.5


### Clone

Primeiro de tudo é necessário clonar o repositório.

```shell
$ git clone https://github.com/vgss/ntiteste.git
```

### Configurações

Após clonar o repositório e a instalação de todas ferramentas, será necessário inicializar o docker no computador.
Quando inicializar, iremos no prompt de comandos e teremos que instalar uma imagem. Para isso iremos digitar esse comando: 
```shell
$ docker pull tomcat:jdk8
```

Agora iremos ver quais imagens existem no docker do nosso computador e pegar o ID da imagem "tomcat:jdk8" digitando o seguinte comando:
> Na coluna IMAGE ID iremos selecionar todo o ID e copiar
```shell
$ docker images
```

Com isso iremos inicializar o nosso container digitando o seguinte comando:
> Depois de dar o comando a baixo será possivel entrar no localhost:9292 e verificar que nosso container já está funcional!
```shell
$ docker run -p 9292:8080 <numero_da_image_id>
```

#### Já temos o nosso container funcionando, agora precisamos colocar nossa aplicação para funcionar nele.

Será necessário que deixe o prompt que você executou aberto e abra outro prompt.
Após isso, digite o seguinte comando no prompt e copie o CONTAINER ID do qual você acabou de criar:
> Caso exista mais de 1 container, copie o CONTAINER ID no qual tem na coluna PORTS escrito: 0.0.0.0:9292->8080/tcp
```shell
$ docker container ls
```
Depois de copiado o CONTAINER ID, iremos executar o seguinte comando e após executado será necessário digitar exit pressionar enter.
```shell
$ docker container exec -it <numero_do_container_id> bash
...
exit
```
Assim iremos precisar copiar a PATH do arquivo simple-app.war encontrado dentro do projeto e digitar esse comando no prompt:
> Para encontrar esse arquivo simple-app.war é necessário seguir essas pastas:
> projeto -> build -> libs -> simple-app.war
```shell
$ docker cp '<PATH>' <CONTAINER_ID>:'/usr/local/tomcat/webapps/'
```
Assim teremos a nossa aplicação rodando no container, basta entrar no browser na url: localhost:9292/simple-app

## Vídeo para melhor avaliação: https://drive.google.com/file/d/1SRJ3ivj0pKB8htr9WiRblndpwSE-vpfM/view?usp=sharing
---

## Testes

Os testes tiveram como objetivo verificar a existência de erros na aplicação.
- Foi criado uma classe "Nti", onde a mesma possui todos os métodos necessários para fazer a automatização utilizando o Selenium.
- Cada teste tem uma função especifica, onde é necessário apenas executar o arquivo .py e assim o teste retornará se passou ou não no teste.


### Retornos:
- Se o teste retornar GREEN é porque a funcionalidade está retornando o valor esperado.
- Se o teste retornar RED é porque a funcionalidade não está retornando o valor esperado.

### Ferramentas necessárias e suas versões

- Python 3.7
- Selenium webdriver
- Geckodriver

## Cenário: Verificação de Login

- Como a aplicação exige de uma autenticação é importante garantir o maximo de cobertura sob essa funcionalidade para que não exista meios de acessar as funcionalidades de admin e de user sem ter acesso ao login.

### Teste 1

- Fazer login com o USERNAME: user e o PASSWORD: user.
> Resultado esperado: Fazer login com sucesso.

- Vídeo do teste 1: https://drive.google.com/open?id=1F366hIs1j4ER3jxNagAQn9TCT1-akftu

### Teste 2

- Fazer login com o USERNAME: admin e o PASSWORD: admin.
> Resultado esperado: Fazer login com sucesso.

- Vídeo do teste 2: https://drive.google.com/open?id=17HLxm_qZZlXhYpzCS56lX3mBgQd93v_-

### Teste 3

- Fazer login com o USERNAME: user e o PASSWORD: 123.
> Resultado esperado: Não fazer login com sucesso.

- Vídeo do teste 3: https://drive.google.com/open?id=13Znm3hS9yQdZ38mNz5tMGkONT74fTItl

### Teste 4

- Fazer login com o USERNAME: teste e o PASSWORD: teste.
> Resultado esperado: Fazer login com sucesso.

- Vídeo do teste 4: https://drive.google.com/open?id=1Q_yunEFnIty0zw-p_VpZ2iBoqcmh-0XH
