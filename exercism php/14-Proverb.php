<?php

declare(strict_types=1);

class Proverb
{
    public function recite(array $list): array
    {
        if (empty($list)) {
            return [];
        }

        $text = [];
        
        for ($i = 0; $i < count($list) - 1; $i++) {
            $text[] = "For want of a " . $list[$i] . " the " . $list[$i + 1] . " was lost.";
        }

        $text[] = "And all for the want of a " . $list[0] . ".";

        return $text;
    }
}