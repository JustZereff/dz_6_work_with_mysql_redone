SELECT 
    t.fullname AS fullname_teacher,
    d.name,
        AVG(g.grade) AS Average_Grade
FROM teachers t
JOIN disciplines d ON t.id = d.teacher_id
JOIN grades g ON d.id = g.discipline_id
WHERE t.id = ?
GROUP BY t.id

;
