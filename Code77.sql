--This soluton willnot cover cases where this word is at the end of the sentence eg. 'Its a bull'.


with words as
(
select filename, (length(contents) - length (replace(contents, ' bull ','')))/length(' bull ') as bull, (length(contents) - length (replace(contents, ' bear ','')))/length(' bear ') as bear from google_file_store
)

select 'bull',(select sum(bull) from words)
union
select 'bear',(select sum(bear) from words)


----------

select word_per_file,count(word_per_file) from (select filename, unnest(string_to_array(contents, ' ')) word_per_file from google_file_store) a where word_per_file in ('bull','bear') group by 1