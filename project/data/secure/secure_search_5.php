<?php
// Secure code: Uses prepared statements for search query
$search = $_GET['search'];

$conn = new mysqli("localhost", "root", "", "test_db");
$query = $conn->prepare("SELECT * FROM products WHERE name LIKE ?");
$search_param = "%$search%";
$query->bind_param("s", $search_param);
$query->execute();
$result = $query->get_result();

while ($row = $result->fetch_assoc()) {
    echo htmlspecialchars($row['name']);
}
?>
