from modulo_pytest.main import guardar_usuario

def test_guardar_usuario(mocker) -> None:
    mock_connect = mocker.patch("sqlite3.connect")
    mock_cursor = mock_connect.return_value.cursor.return_value

    guardar_usuario("Ana", 27)

    mock_cursor.execute.assert_called_once_with(
        "INSERT INTO usuarios (nombre, edad) VALUES (?, ?)",
        ("Ana", 27)
    )
    mock_connect.return_value.commit.assert_called_once()
    mock_connect.return_value.close.assert_called_once()


# mocker.patch("os.remove")
# mocker.patch.object(os, "listdir")
