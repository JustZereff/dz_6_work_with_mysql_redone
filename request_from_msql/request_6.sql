SELECT fullname AS fullname_student
FROM students s
JOIN groups g ON s.group_id = g.id
WHERE g.name = ?
;
