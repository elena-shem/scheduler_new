<?php
$db_path = __DIR__ . '/fuel/app/scheduler_new.sqlite';
try {
    $db = new PDO('sqlite:' . $db_path);
    $db->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);

    // Добавление deleted_at
    $db->exec('ALTER TABLE professors ADD COLUMN deleted_at INTEGER NULL;');
    echo "Колонка deleted_at добавлена в professors.\n";

    $db->exec('ALTER TABLE doctorals ADD COLUMN deleted_at INTEGER NULL;');
    echo "Колонка deleted_at добавлена в doctorals.\n";

    // Создание отсутствующей таблицы
    $db->exec('CREATE TABLE IF NOT EXISTS exam_supervisions (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        doctoral_id INTEGER NULL,
        examcourse_id INTEGER NULL,
        hours INTEGER NULL,
        attended INTEGER DEFAULT 0,
        comment TEXT NULL,
        custom_exam_day TEXT NULL,
        custom_exam_hour TEXT NULL,
        created_at INTEGER NULL,
        updated_at INTEGER NULL
    );');
    echo "Таблица exam_supervisions создана.\n";

} catch (Exception $e) {
    echo "Ошибка: " . $e->getMessage() . "\n";
}