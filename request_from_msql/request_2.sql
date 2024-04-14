SELECT 
        s.fullname AS student_name, 
        d.name,
            AVG(g.grade) AS average_grade
FROM students s
JOIN grades g ON s.id = g.student_id
JOIN disciplines d ON g.discipline_id = d.id
WHERE d.name = ?
GROUP BY s.id
ORDER BY average_grade DESC
LIMIT 1;
