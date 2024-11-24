<?php

declare(strict_types=1);

class ResistorColorDuo
{
    public function getColorsValue(array $colors): int
    {
        $colorValues = [
            "black" => 0,
            "brown" => 1,
            "red" => 2,
            "orange" => 3,
            "yellow" => 4,
            "green" => 5,
            "blue" => 6,
            "violet" => 7,
            "grey" => 8,
            "white" => 9,
        ];

        $arr = [$colors[0], $colors[1]];
        $total = 0;

        for ($i = 0; $i < count($arr); $i++) {
            $multiplier = 10 ** (1 - $i);
            
            if (!isset($colorValues[$arr[$i]])) {
                throw new InvalidArgumentException("Invalid color: {$arr[$i]}");
            }
            $total += $colorValues[$arr[$i]] * $multiplier;
        }
        return $total;
    }
}