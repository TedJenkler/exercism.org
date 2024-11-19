<?php

function language_list(...$strings)
{
    return $strings;
}

function add_to_language_list($array, $language) 
{
    $array[] = $language;
    return $array;
}

function prune_language_list($array)
{
    array_shift($array);
    return $array;
}

function current_language($strings) 
{
    return $strings[0];
}

function language_list_length($strings)
{
    return count($strings);
}