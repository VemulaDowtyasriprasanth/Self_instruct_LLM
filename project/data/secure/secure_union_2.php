<?php
// Secure code: Input validation and prepared statements
$id = $_GET['id'];

if (!filter_var($id, FILTER_VALIDATE_INT)) {
    die("Invalid input");
}

$conn = new mysqli("localhost", "root", "", "test_db");
$query = $conn->prepare("SELECT name FROM users WHERE id = ?");
$query->bind_param("i", $id);
$query->execute();
$result = $query->get_result();

while ($row = $result->fetch_assoc()) {
    echo htmlspecialchars($row['name']);
}
?>
