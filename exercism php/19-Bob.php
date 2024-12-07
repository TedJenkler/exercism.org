<?php

declare(strict_types=1);

class Bob
{
    public function respondTo(string $str): string
    {
        $trimmed = trim($str);
        if($trimmed[-1] == "?" && strtoupper($str) === $str && preg_match("/[a-zA-Z]/", $str)) {
            return "Calm down, I know what I'm doing!";
        }
        elseif($trimmed[-1] == "?") {
            return "Sure.";
        }
        elseif(strtoupper($str) === $str && preg_match("/[a-zA-Z]/", $str)) {
            return "Whoa, chill out!";
        }
        elseif($trimmed === "") {
            return "Fine. Be that way!";
        }
        return "Whatever.";
    }
}

?>