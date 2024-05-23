# Висновки щодо швидкостей алгоритмів пошуку підрядків

## Алгоритми та текст 1

- **Існуючий підрядок:** "index"
  - **KMP:** 0.000951 seconds
  - **Boyer-Moore:** 0.000626 seconds
  - **Rabin-Karp:** 0.002462 seconds
- **Неіснуючий підрядок:** "victory"
  - **KMP:** 0.006717 seconds
  - **Boyer-Moore:** 0.001685 seconds
  - **Rabin-Karp:** 0.009968 seconds

## Алгоритми та текст 2

- **Існуючий підрядок:** "index"
  - **KMP:** 0.005519 seconds
  - **Boyer-Moore:** 0.003049 seconds
  - **Rabin-Karp:** 0.014032 seconds
- **Неіснуючий підрядок:** "victory"
  - **KMP:** 0.004686 seconds
  - **Boyer-Moore:** 0.002302 seconds
  - **Rabin-Karp:** 0.013035 seconds

## Загальні висновки

- Найшвидший алгоритм для тексту 1: Boyer-Moore
- Найшвидший алгоритм для тексту 2: Boyer-Moore
- Загальний найшвидший алгоритм: Boyer-Moore
