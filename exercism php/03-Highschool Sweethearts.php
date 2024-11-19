<?php

class HighSchoolSweetheart
{
    public function firstLetter(string $name): string
    {
        return substr(trim($name), 0, 1); // First letter of the name
    }

    public function initial(string $name): string
    {
        return ucfirst($this->firstLetter($name)) . "."; // Capitalized first letter with a dot
    }

    public function initials(string $name): string
    {
        $arr = explode(" ", $name); // Split first and last name
        return $this->initial($arr[0]) . " " . $this->initial($arr[1]);
    }

    public function pair(string $name1, string $name2): string
    {
        $initials1 = self::initials($name1);
        $initials2 = self::initials($name2);

        $initials = "$initials1  +  $initials2";

        $heart = <<<HEART
             ******       ******
           **      **   **      **
         **         ** **         **
        **            *            **
        **                         **
        **     {$initials}     **
         **                       **
           **                   **
             **               **
               **           **
                 **       **
                   **   **
                     ***
                      *
        HEART;

        return $heart;
    }
}