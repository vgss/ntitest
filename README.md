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



-
