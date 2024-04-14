SELECT DISTINCT 
    d.name AS Course_Name
FROM disciplines d
JOIN grades g ON d.id = g.discipline_id
WHERE g.student_id = ?
;