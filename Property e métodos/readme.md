# Exercícios de Programação Orientada a Objetos com Python

Este README reúne exercícios do curso de **Programação Orientada a Objetos com Python da Alura**.

O objetivo é praticar conceitos de classes, construtores, atributos protegidos, métodos especiais, propriedades, métodos de instância e métodos de classe.

As respostas dos exercícios estão organizadas em arquivos separados, e cada arquivo corresponde ao exercício indicado abaixo.

---

## Exercício 1

**Arquivo de resposta:** `conta_bancaria.py`

Crie uma classe chamada `ContaBancaria` com um construtor que aceita os parâmetros `titular` e `saldo`.

O atributo `ativo` deve iniciar como `False` por padrão.

---

## Exercício 2

**Arquivo de resposta:** `conta_bancaria_1.py`

Na classe `ContaBancaria`, adicione um método especial `__str__`.

Esse método deve retornar uma mensagem formatada com o titular e o saldo da conta.

Depois, crie duas instâncias da classe e imprima essas instâncias.

---

## Exercício 3

**Arquivo de resposta:** `conta_bancaria_2.py`

Adicione um método chamado `ativar_conta` à classe `ContaBancaria`.

Esse método deve definir o atributo `ativo` como `True`.

Depois, crie uma instância da classe, chame o método e imprima o valor de `ativo`.

---

## Exercício 4

**Arquivo de resposta:** `conta_bancaria_pythonica.py`

Refatore a classe `ContaBancaria` para utilizar a abordagem mais “pythonica” na criação de atributos.

Utilize propriedades, se necessário.

---

## Exercício 5

**Arquivo de resposta:** `conta_bancaria_pythonica_1.py`

Crie uma instância da classe `ContaBancariaPythonica`.

Depois, imprima o valor da propriedade `titular`.

---

## Exercício 6

**Arquivo de resposta:** `cliente_banco.py`

Crie uma classe chamada `ClienteBanco` com um construtor que aceita 5 atributos.

Depois, instancie 3 objetos dessa classe e atribua valores aos seus atributos através do método construtor.

---

## Exercício 7

**Arquivo de resposta:** `cliente_banco_1.py`

Crie um método de classe para a classe `ClienteBanco`.

Esse método deve ser responsável por criar uma conta bancária para um cliente.