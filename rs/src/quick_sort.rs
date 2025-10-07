pub fn quick_sort(arr: &mut Vec<i32>, p: usize, r: usize) {
    if p < r {
        let q = partition(arr, p, r);
        if p < q {
            quick_sort(arr, p, q-1);
        }
        quick_sort(arr, q+1, r);
    }
}

fn partition(arr: &mut Vec<i32>, p: usize, r: usize) -> usize {
    let pivot = *arr.get(r).unwrap();
    let mut l = p;
    for i in p..r {
        let curr = *arr.get(i).unwrap();
        if curr <= pivot {
            *arr.get_mut(i).unwrap() = *arr.get(l).unwrap();
            *arr.get_mut(l).unwrap() = curr;
            l += 1;
        }
    }

    *arr.get_mut(r).unwrap() = *arr.get(l).unwrap();
    *arr.get_mut(l).unwrap() = pivot;

    l
}

#[cfg(test)]
pub mod tests {
    use super::*;

    #[test]
    fn test() {
        let mut li = Vec::from([0, 10, -3, 5, 4]);
        let len = li.len();
        quick_sort(&mut li, 0, len-1);

        let mut t = *li.get(0).unwrap();
        for i in li {
            assert!(t <= i, "expected {} to be smaller or equal than {}", t, i);
            t = i;
        }
    }
}
