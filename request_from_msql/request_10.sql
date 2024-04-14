SELECT DISTINCT 
    d.name AS Course_Name
FROM disciplines d
JOIN grades g ON d.id = g.discipline_id
JOIN students s ON g.student_id = s.id
JOIN teachers t ON d.teacher_id = t.id
WHERE
    s.id = ?
  AND
    t.id = ?
;
