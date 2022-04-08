<?php 
  spl_autoload_register(function (string $nomeClasse) {
      $arquivo = str_replace('D23004\\Software', 'Software', $nomeClasse);
      $arquivo = str_replace('\\', DIRECTORY_SEPARATOR, $arquivo);
      $arquivo .= '.php';

      if (file_exists($arquivo)) {
          require_once $arquivo;
      }
  });
?>