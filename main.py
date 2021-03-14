from math import ceil


class Product:
    def __init__(self, name, sm_cap, md_cap, lg_cap):
        self.name = name
        self.sm_cap = sm_cap
        self.md_cap = md_cap
        self.lg_cap = lg_cap

    def pack_order(self, quantity: int) -> dict:
        sm_box = 0
        md_box = 0
        lg_box = 0
        full_lg_box, lg_mod = divmod(quantity, self.lg_cap)
        if full_lg_box == 1:
            if lg_mod > 3:
                lg_box = 2
            elif lg_mod > 0:
                md_box = 2
            else:
                lg_box = 1
        else:
            lg_box = full_lg_box
            if lg_mod > self.md_cap:
                lg_box = full_lg_box + 1
            else:
                full_md_box, md_mod = divmod(lg_mod, self.md_cap)
                md_box = full_md_box
                if md_mod > self.sm_cap:
                    md_box = 1
                else:
                    full_sm_box, sm_mod = divmod(md_mod, self.sm_cap)
                    sm_box = full_sm_box
                    if sm_mod:
                        sm_box = 1
        col_box = self.return_col_box(sm_box, md_box, lg_box)
        return self.return_info(sm_box, md_box, lg_box, col_box)

    def return_col_box(self, sm_box: int, md_box: int, lg_box: int) -> int:
        sum_el = sum([sm_box * self.sm_cap, md_box * self.md_cap, lg_box * self.lg_cap])
        if sum_el <= 9:
            col_box = 0
        else:
            col_box = ceil(sum_el / 27)
        return col_box

    @staticmethod
    def return_info(sm_box: int, md_box: int, lg_box: int, col_box: int) -> dict:
        return {"small_cardboard_box": sm_box,
                "medium_cardboard_box": md_box,
                "large_cardboard_box": lg_box,
                "collect_cardboard_box": col_box}


if __name__ == '__main__':
    p = Product("A", 3, 6, 9)
    print(p.pack_order(12))
