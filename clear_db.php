<?php
$db_path = __DIR__ . '/fuel/app/scheduler_new.sqlite';
try {
    $db = new PDO('sqlite:' . $db_path);
    $db->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);

    // Получаем список всех созданных таблиц, исключая системные
    $result = $db->query("SELECT name FROM sqlite_master WHERE type='table' AND name NOT LIKE 'sqlite_%'");
    
    foreach ($result as $row) {
        $table = $row['name'];
        // Удаляем все строки из таблицы
        $db->exec("DELETE FROM `$table`;");
        echo "Таблица очищена: $table\n";
    }

    // Сбрасываем счетчики автоинкремента (ID снова начнутся с 1)
    $db->exec("DELETE FROM sqlite_sequence;");
    
    // Оптимизируем файл БД и освобождаем место
    $db->exec("VACUUM;");

    echo "\nВсе данные удалены. Структура БД готова к миграции.\n";
} catch (Exception $e) {
    echo "Ошибка: " . $e->getMessage() . "\n";
}