#### Затраты времени на 10 000 и 100 000 операций, мс

Модуль|Вставка начало|Вставка по случайному индексу|Вставка конец|Чтение начало|Чтение по индекту|Чтение конец|Удаление начало|Удаление по индексу|Удаление конец 
---|---:|---:|---:|---:|---:|---:|---:|---:|---:
singleArray(10 000)|107|107|95|0|2|0|28|32|30
singleArray(100 000)|3463|2990|2864|0|4|1|2193|2610|2172
vectorArray(10 000)|19|15|14|0|2|1|12|5|1
vectorArray(100 000)|896|637|610|0|4|1|573|235|4
factorArray(10 000)|6|14|2|0|6|1|4|4|0
factorArray(100 000)|571|290|5|0|3|0|565|244|4
matrixArray(10 000)|245|124|4|0|2|0|220|170|3
matrixArray(100 000)|19727|10417|109|0|8|3|17475|8507|37

#### singleArray
Занимает мало памяти. Быстрое чтение по индексу.
С увеличение длины массива время на удаление и вставку значительно растет.
#### vectorArray
Почти тоже, что и в singleArray, но копирование происходит только при переполнении вектора.
Занимает памяти немного больше, чем singleArray.
#### factorArray
Так же, как и в предыдущем варианте, котипование происходит не всегда, а при переполнении вектора, который увеличивается пропорционально уже выделенной памяти.
#### matrixArray
При вставке или удалении приводит к большому числу копирований. Очень медленный.