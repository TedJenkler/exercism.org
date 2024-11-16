<?php

class AnnalynsInfiltration
{
    public function canFastAttack($is_knight_awake)
    {
        return !$is_knight_awake;
    }

    public function canSpy(
        $is_knight_awake,
        $is_archer_awake,
        $is_prisoner_awake
    ) {
        return $is_knight_awake || $is_archer_awake || $is_prisoner_awake;
    }

    public function canSignal(
        $is_archer_awake,
        $is_prisoner_awake
    ) {
        return $is_prisoner_awake && !$is_archer_awake;
    }

    public function canLiberate(
        $is_knight_awake,
        $is_archer_awake,
        $is_prisoner_awake,
        $is_dog_present
    ) {
        if($is_dog_present && !$is_archer_awake) {
            return true;
        }
        else if(!$is_dog_present && $is_prisoner_awake && !$is_archer_awake && !$is_knight_awake) {
            return true;
        }
        else {
            return false;
        }
    }
}