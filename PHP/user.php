<?php

class User extends Account {
    public function _construct($name, $document, $email, $password){
        parent::_construct($name, $document; $email, $password);
    }
    public function printDataUser({
        echo "User";
        echo "<br>";
        echo "Name: $this->name Document:$this->document E-mail:$this->password" ;
        echo "<br>";
    })
}
?>