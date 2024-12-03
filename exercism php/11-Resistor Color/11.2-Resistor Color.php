<?php

declare(strict_types=1);

function getAllColors(): array
{
    return ['black', 'brown', 'red', 'orange', 'yellow', 'green', 'blue', 'violet', 'grey', 'white'];
}

function colorCode(string $color): int
{
    $arr = getAllColors();
    for($i = 0; $i < count($arr); $i++) {
        if($arr[$i] == $color) {
            return $i;
        }
    }
}

?>