#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

#define GET_ARRAY_LEN(len, array) { len = sizeof(array) / sizeof(array[0]);}

int * initilize_id_array(void);
int quick_find_find(int n, const int * id);
int quick_union_find(int n, const int * id);
void quick_union_union(int p, int q, int * id, int id_len);
void quick_find_union(int p, int q, int * id, int id_len);
void weighted_quick_union_union(int p, int q, int * id, int * sz, int id_len);

int main(int argc, char const* argv[]){
    const int connections[][2] = {
        {3, 4}, {4, 9}, {8, 0}, {2, 3},
        {5, 6}, {2, 9}, {5, 9}, {7, 3},
        {4, 8}, {5, 2}, {0, 2}, {6, 1}
    };
    int * id = NULL;
    int id_len = 10;
    int connections_len = 0;
    int sz[10] = {1, 1, 1, 1, 1, 1, 1, 1, 1, 1};

    GET_ARRAY_LEN(connections_len, connections);

    printf("Quick find method:\n");
    id = initilize_id_array();
    for (int i = 0; i < connections_len; i++) {
        printf("%02d:", i + 1);
        quick_find_union(connections[i][0], connections[i][1], id, id_len);
    }
    free(id);

    printf("Quick union method:\n");
    id = initilize_id_array();
    for (int i = 0; i < connections_len; i++) {
        printf("%02d:", i + 1);
        quick_union_union(connections[i][0], connections[i][1], id, id_len);
    }
    free(id);

    printf("Quick union method:\n");
    id = initilize_id_array();
    for (int i = 0; i < connections_len; i++) {
        printf("%02d:", i + 1);
        weighted_quick_union_union(connections[i][0], connections[i][1], id, sz, id_len);
    }
    free(id);

    return 0;
}

int * initilize_id_array(void){
    int * new = (int *)malloc(sizeof(int) * 10);
    for (int i = 0;i < 10; i++)
        new[i] = i;
    return new;
}

int quick_find_find(int n, const int * id){
    return id[n];
}

void quick_find_union(int p, int q, int * id, int id_len){
    int len = 0;
    int q_id = quick_find_find(p, id);
    int p_id = quick_find_find(q, id);

    if (q_id == p_id) {
        printf("\n");
        return;
    }
    for (int i = 0; i < id_len; i++) {
        if (id[i] == p_id) {
            id[i] = q_id;
        }
    }
    printf("%d %d\n", p, q);
}

// search the parent node in the tree
int quick_union_find(int n, const int * id){
    while ( n != id[n]) {
        n = id[n];
    }

    return n;
}

void quick_union_union(int p, int q, int * id, int id_len){
    int p_root = quick_union_find(p, id);
    int q_root = quick_union_find(q, id);

    if (p_root == q_root) {
        printf("\n");
        return;
    }
    printf("%d %d\n", p, q);
    id[p_root] = q_root; 
}

void weighted_quick_union_union(int p, int q, int * id, int * sz, int id_len){
    int p_root = quick_union_find(p, id);
    int q_root = quick_union_find(q, id);

    if (q_root == p_root){
        printf("\n");
        return;
    }
    printf("%d %d\n", p, q);
    if (sz[p_root] < sz[q_root]){
        id[p_root] = q_root;
        sz[q_root] += sz[p_root];
    } else {
        id[q_root] = p_root;
        sz[p_root] += sz[q_root];
    }
}
