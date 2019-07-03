# Ключехранитель паролейX 
## Описание:
`Этот мужчина был настолько доволен собой, что использовал своё имя в качестве секретного ключа для хранилища паролей. Узнай, что же такое он там скрывает?`

Инфа для новичков:
`http://www.harmj0y.net/blog/redteaming/a-case-study-in-attacking-keepass/`

## Решение:
`Используем утилиту John'а keepass2john и получаем хеш от криптоконтейнера, затем с помощью словаря паролей и hashcat/john получаем пароль от базы. Внутри контейнера лежит флаг.`

## Флаг:
`PermCTF{rubber_hose_crypanalysis}`