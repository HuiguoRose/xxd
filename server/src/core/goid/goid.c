// +build !go1.4

#include "runtime.h"

void ·GetGoroutineId(int64 ret) {
	ret = g->goid;
	USED(&ret);
}
