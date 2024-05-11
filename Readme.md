## GoPy Example

### Install & build

```sh
just install && just build
```

### Fibonacci timeit default bench

```sh
bench
```

**100** GoPy **fast**: `0.5463700420077657` sec\
**100** Python **fast**: `2.31602508299693` sec

**200** GoPy **fast**: `0.33885920800094027` sec\
**200** Python **fast**: `4.890809417003766` sec

**300** GoPy **fast**: `0.38037749999784864` sec\
**300** Python **fast**: `7.483160250005312` sec

**10** GoPy **recursive**: `0.4290675829979591` sec\
**10** Python **recursive**: `8.46965845899831` sec

**15** GoPy **recursive**: `2.1352655829978175` sec\
**15** Python **recursive**: `95.43500908400165` sec
