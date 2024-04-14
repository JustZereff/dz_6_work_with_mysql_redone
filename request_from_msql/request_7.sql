SELECT s.fullname AS fullname_student, g.grade AS grade
FROM students s
JOIN grades g ON s.id = g.student_id
JOIN disciplines d ON g.discipline_id = d.id
JOIN groups gr ON s.group_id = gr.id
WHERE 
    gr.name = ?
  AND 
    d.name = ?
;
