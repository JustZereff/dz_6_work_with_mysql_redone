SELECT DISTINCT d.name AS Course_Name
FROM disciplines d
JOIN teachers t ON d.teacher_id = t.id
WHERE t.id = ?
;