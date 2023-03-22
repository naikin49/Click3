#pragma once

#define DLL_EXPORT __declspec(dllexport) 
extern "C"  DLL_EXPORT void Find_Img(int, int*, int*, int, int, int, int, int*, int*);