# word_calculator
## или второй проект для вузовского практикума

*русский словесный калькулятор*

### описание проекта ✍️
вывод результата вычисления числового выражения, записанного русскими словами. в процессе реализации были использованы *(вежливо позаимствованы)* сторонние библиотеки и модули: 
1) num2words для перевода чисел в русские слова
2) word2number для перевода англ слова в число.
3) googletrans использован для перевода русского слова в англ. тут стоит отметь, что модуль постоянно обновляется, из-за этого возможны сбои в работе моего калькулятора. для их устроения требуется всего лишь обновить версию данного модуля *(но иногда даже обнволение версии не помогает :))*.

две основных функции:
1) calculator_base(line) решает простейший пример в одно действие
2) calculator_long_puzzle(line) решает пример в несколько действий



### структура репозитория 🤖
1) файл requirements.txt с перечнем использованных модулей и их конкретных версий
2) основной файл с кодом main.py, который запускает игру

      
 ### пара слов от автора 🤡
гениальным было решение использовать сторонние модули для облегчения задачи. кроме того, был полностью переработан алгоритм счёта. но риски есть риски, и код не всегда запускается без ошибок :с
