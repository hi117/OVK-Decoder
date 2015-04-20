This program decodes .ovk files used in the Reallive engine and the Siglius engine.

File format:
    4 byte little endian file count (= n)
    n * struct table entry
    n * embedded files

struct tableEntry
{
    int length;
    int offset;
    int unk1;
    int unk2;
};
