#include <stdio.h>
int value4AGTC(char chr);
int assign_id(char n1,char n2,char n3);
char id_to_protein(int id);
int main(void) {
    char dna[3001];
    char protein[3001];
    int i=0,j=0,k=0,m=0;
    int result[4];
    int id1,id2;
    int ch;
    int h=1;
    int consumed=0,fullconsumed=0;
    /* read DNA */
    ch=getchar();
    dna[0]=(char)ch;
    do
    {
        ch=getchar();
        if(ch==' ' || ch=='\n' || ch=='\t')
            continue;
        dna[h]=(char )ch;
        h++;
    }while (ch != '.');
    /* read protein */
    h=0;
    ch=getchar();
    protein[0]=(char)ch;
    do
    {
        ch=getchar();
        if(ch==' ' || ch=='\n' || ch=='\t')
            continue;
        protein[h]=(char )ch;
        h++;
    }while (ch != '.');
    /* check start of DNA matches start of protein */
    id1=assign_id(dna[i],dna[i+1],dna[i+2]);
    if(id_to_protein(id1)!=protein[j])
    {
        printf("NONE");
        return 0;
    }
    while (id_to_protein(id1)==protein[j])
    {
        i+=3;
        j++;
        id1=assign_id(dna[i],dna[i+1],dna[i+2]);
    }
    /* find end of DNA */
    while (dna[k]!='.')
    {
        k++;
    }
    k-=4; /* skip  stop codon */
    /* check last three nucleotide correspond stop codon */
    if(id_to_protein(assign_id(dna[k+1],dna[k+2],dna[k+3]))!='!')
    {
        printf("NONE");
        return 0;
    }
    /* find end of protein */
    while (protein[m]!='.')
    {
        m++;
    }
    m--;
    /* check head of DNA matches with whole protein */
    if(j-m==1)
    {
        j-=2;
        fullconsumed=1;
    }
    /* check end of DNA matches end of protein */
    id2=assign_id(dna[k-2],dna[k-1],dna[k]);
    if(id_to_protein(id2)!=protein[m])
    {
        /*result[3]=k;*/
        /*printf("here\n");*/
    }
    while (id_to_protein(id2)==protein[m])
    {
        k-=3;
        m--;
        if (j-m==1)
        {
            consumed=1; /* consumed is true when start and end of dna and protein match */
            break;
        }
        id2=assign_id(dna[k-2],dna[k-1],dna[k]);
    }
    if (consumed)
    {   int a,match=0;

        for ( a = i-2; a <=k-3 ; a++) {
            id1=assign_id(dna[a],dna[a+1],dna[a+2]);
            if(id_to_protein(id1)==protein[j-1])
            {
                result[1]=a-1;
                result[2]=a+3;
                result[0]=i-3;
                result[3]=k;
                if(fullconsumed)
                {
                    result[0]-=3;
                    result[3]+=3;
                }
                match=1;
                break;
            }
        }
        if(!match)
        {
            for ( a = i+1; a <=k ; a++) {
                id1=assign_id(dna[a],dna[a+1],dna[a+2]);
                if (id_to_protein(id1)==protein[m+1])
                {
                    result[1]=a-1;
                    result[2]=a+3;
                    result[0]=i;
                    result[3]=k+3;
                    match=1;
                    break;
                }
            }
        }
        if(!match)
        {
            printf("NONE");
            return 0;
        }

    }
    /* normal cases : there are 3 exon separately */
    else {
        result[0] = i;
        result[3] = k;
        /* search until second exon from head */
        while (id_to_protein(id1) != protein[j]) {
            i++;
            if (i > k) {
                printf("NONE");
                return 0;
            }
            id1 = assign_id(dna[i], dna[i + 1], dna[i + 2]);
        }
        /* search until second exon from end */
        while (id_to_protein(id2) != protein[m]) {
            k--;
            id2 = assign_id(dna[k - 2], dna[k - 1], dna[k]);
        }
        result[1] = i - 1;
        result[2] = k + 1;
        while (i <= k) {
            int count = 0;
            int flag = 0;
            while (id_to_protein(id1) == protein[j]) {
                i += 3;
                j++;
                count++;
                if (j > m) {
                    result[2] = i;
                    flag = 1; /* match is completed */
                    break;
                }
                id1 = assign_id(dna[i], dna[i + 1], dna[i + 2]);
            }
            if (flag == 1)
                break;
            if (k - i == 2) {
                result[2] = k + 1;
                break;
            } else
                j -= count; /* some part matched but not all  protein so turn back*/
            /* shift until finding matching amino acid  */
            while (id_to_protein(id1) != protein[j]) {
                if(i>k)
                {
                    printf("NONE");
                    return 0;
                }
                i++;
                id1 = assign_id(dna[i], dna[i + 1], dna[i + 2]);
            }
            result[1] = i - 1;
        }
    }
    printf("%d %d %d %d",result[0],result[1],result[2],result[3]);
    return 0;
}
int assign_id(char n1,char n2,char n3)
{
    int id;
    id=value4AGTC(n1)*16+ value4AGTC(n2)*4+ value4AGTC(n3);
    return id;
}
char id_to_protein(int id)
{
    if (id==50 || id ==52 ||id==65 || id==66 || id==67 || id==68)
        return 'r';
    else if (id==22 || id ==24 ||id==53 || id==54 || id==55 || id==56)
        return 'l';
    else if (id==29 || id ==30 ||id==31 || id==32 || id==49 || id==51)
        return 's';
    else if (id==61 || id ==62 ||id==63 || id==64)
        return 'p';
    else if (id==81 || id ==82 ||id==83 || id==84)
        return 'g';
    else if (id==77 || id ==78 ||id==79 || id==80)
        return 'a';
    else if (id==69 || id ==70 ||id==71 || id==72)
        return 'v';
    else if (id==45 || id ==46 ||id==47 || id==48)
        return 't';
    else if (id==37 || id ==38 ||id==39)
        return 'i';
    else if (id==26 || id ==28 ||id==34)
        return '!';  /* stop */
    else if (id==73 || id ==75 )
        return 'd';
    else if (id==74 || id ==76 )
        return 'e';
    else if (id==42 || id ==44 )
        return 'k';
    else if (id==41 || id ==43 )
        return 'n';
    else if (id==58 || id ==60 )
        return 'q';
    else if (id==33 || id ==35 )
        return 'c';
    else if (id==21 || id ==23 )
        return 'f';
    else if (id==25 || id ==27 )
        return 'y';
    else if (id==57 || id ==59 )
        return 'h';
    else if (id==40)
        return 'm';
    else if (id==36)
        return 'w';
    else
        return 'x';
}
int value4AGTC(char chr)
{
    switch (chr) {
        case 'A':
            return 1;
        case 'T':
            return 2;
        case 'G':
            return 3;
        case 'C':
            return 4;
        default:
            return 0;
    }
}

