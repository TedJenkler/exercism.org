<?php

declare(strict_types=1);

function distance(string $strandA, string $strandB): int
{
    if (strlen($strandA) !== strlen($strandB)) {
        throw new InvalidArgumentException("strands must be of equal length");
    }

    $arrA = str_split($strandA);
    $arrB = str_split($strandB);

    $count = 0;

    for ($i = 0; $i < count($arrA); $i++) {
        if ($arrA[$i] !== $arrB[$i]) {
            $count++;
        }
    }
    return $count;
}

?>