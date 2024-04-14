SELECT 
    d.name AS Subject_Name, 
    s.group_id AS Group_ID, 
    gr.name AS Group_Name, 
        AVG(g.grade) AS Average_Grade
FROM grades g
JOIN disciplines d ON g.discipline_id = d.id
JOIN students s ON g.student_id = s.id
JOIN groups gr ON s.group_id = gr.id
WHERE d.name = ?
GROUP BY s.group_id, gr.name;
