for i in {1..2}
do
    for j in {0..9}
    do
        for k in {0..9}
        do
#            for suffix in  ''  '-alpha'  '-beta'
            for suffix in  ''
            do
                tag_name=v1.$i.$j.$k$suffix
                res_0=$(git tag -d $tag_name)
                res_1=${res_0:0:3}
                echo ---.$res_1.===
                if [ "$res_1" = "Del" ]; then
                    git push origin :refs/tags/$tag_name
                fi
            done
        done
    done
done
