@echo off
chcp 65001 > nul
echo Генератор документации pdoc
echo.

python -m pdoc ^
  src ^
  homework_3 ^
  homework_4 ^
  homework_5 ^
  homework_6 ^
  homework_7 ^
  homework_8 ^
  lesson_1-2 ^
  lesson_3-4 ^
  lesson_5-6 ^
  lesson_7-8 ^
  lesson_9-10 ^
  lesson_11-12 ^
  lesson_13-14 ^
  lesson_15-16 ^
  -o ./docs ^
  --mermaid ^
  --math ^
  --search ^
  --show-source

echo Документация сгенерирована и добавлена в папку docs\
pause