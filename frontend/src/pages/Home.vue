<template>
  <div class="text-center p-0 m-0 container-fluid">
    <div class="jumbotron m-0 p-0 p-3 jumbotron-fluid">
      <div class="container">
        <h2 class="display-4">Receipt Generator</h2>

        <div class="row mb-10 no-gutters justify-content-center">
          <div id="app-6">
            <input id="inputArea" v-model="message" />
          </div>
          <a id="addBtn"
            @click="onClick"
            rel="noopener"
            target="_blank"
            class="btn btn-success"
          >
            Add
          </a>
        </div>
      </div>
    </div>
    <div class="container">
      <div class="row">
        <div class="col">
          <div
            class="jumbotron text-left m-0 text-dark bg-white border-white border"
          >
            <h2>Order list</h2>
            <div v-for="item in allMessages" :data="item" :key="item">
              > {{ item }}
              <button id="btn" @click="deleteItem(item)">Delete</button>
            </div>
            <a
              @click="getReceiptGenerator"
              rel="noopener"
              target="_blank"
              class="btn btn-success"
            >
              Generate Receipt
            </a>
          </div>
        </div>
        <div class="col">
          <div
            class="jumbotron text-left m-0 text-dark bg-white border-white border"
          >
            <h2 class="display-5">Generated Receipt</h2>
            <div v-for="item in receipts.data" :data="item" :key="item">
              > {{ item }}
            </div>
            <div>> Sales Taxes: {{ receipts.SalesTax }}</div>
            <div>> Total: {{ receipts.Total }}</div>
          </div>
        </div>
      </div>
    </div>
    <a id="refresh"
       @click="refreshAll"
       rel="noopener"
       target="_blank"
       class="btn btn-success"
    >
      Refresh
    </a>
  </div>
</template>

<script lang="ts">
import { Vue, Component } from "@/utils/vue-imports";
import Navbar from "@/components/Navbar.vue";

@Component({
  name: "Home",
  components: {
    Navbar,
  },
})
export default class Home extends Vue {
  message: any = "";
  allMessages: any = [];
  receipts: any = {
    data: [],
    SalesTax: 0,
    Total: 0,
  };
  measurement: any = [
    "bar",
    "bottle",
    "box",
    "can",
    "carton",
    "cup",
    "drop",
    "glass",
    "grain",
    "item",
    "jar",
    "box",
    "bottle",
    "packet",
    "box",
    "piece",
    "roll",
    "slice",
    "spoonful",
    "tablespoon",
    "teaspoon",
    "tube",
  ];
  assignObject(object: any) {
    return {
      item: object.item,
      Itemtype: object.Itemtype,
      TaxType: object.TaxType,
      quantity: object.quantity,
      price: object.price,
    };
  }
  refreshAll() {
    this.allMessages = [];
    this.receipts = {
      data: [],
      SalesTax: 0,
      Total: 0,
    };
  }
  deleteItem(item: any) {
    const idImport = this.allMessages.indexOf(item);
    this.allMessages.splice(idImport, 1);
  }
  tokenizer(string: any) {
    const words: any = string.split(" ");
    const originalString = words.slice(0, -2).join(" ");
    const quantity = words[0];
    const price = words.slice(-1)[0];
    let importType = "local_item";
    const priceFloat = parseFloat(price);
    const idQuantity = words.indexOf(quantity);
    words.splice(idQuantity, 1);
    if (words.includes("at")) {
      const idAt = words.indexOf("at");
      words.splice(idAt, 1);
    }
    if (words.includes("imported")) {
      const idImport = words.indexOf("imported");
      words.splice(idImport, 1);
      importType = "imported_item";
    }
    if (words.includes("of")) {
      const idOf = words.indexOf("of");
      words.splice(idOf, 1);
    }
    const idPrice = words.indexOf(price);
    words.splice(idPrice, 1);
    for (const word of this.measurement) {
      if (words.includes(word)) {
        const idWord = words.indexOf(word);
        words.splice(idWord, 1);
      }
    }

    return {
      item: words.join(" "),
      originalString: originalString,
      TaxType: importType,
      quantity: quantity,
      price: priceFloat,
    };
  }
  async getReceiptGenerator() {
    for (const string of this.allMessages) {
      const order: any = this.tokenizer(string);
      let type = null;
      try {
        type = await this.getType(order.item);
      } finally {
        order.Itemtype = type;
        const final = await this.makeApiCalls(this.assignObject(order));
        this.receipts.SalesTax = this.receipts.SalesTax + final.tax;
        this.receipts.Total = this.receipts.Total + final.total;
        const stringToAdd = order.originalString + ": " + final.total;
        this.receipts.data.push(stringToAdd);
      }
    }
    this.receipts.SalesTax = (Math.ceil(this.receipts.SalesTax*20)/20).toFixed(2)
  }
  async getType(item: any) {
    let data = null;
    const response = await fetch(
      `${process.env.VUE_APP_ROOT_API}/taxCal/?itemInput=${item}`,
      {
        method: "GET",
        headers: {
          "content-type": "application/json",
        },
      }
    );

    // Storing data in form of JSON
    data = await response.json();
    return data.item;
  }
  async makeApiCalls(items: any) {
    let data = null;
    const response = await fetch(`${process.env.VUE_APP_ROOT_API}/taxCal`, {
      method: "POST",
      headers: {
        "content-type": "application/json",
      },
      body: JSON.stringify(items),
    });

    // Storing data in form of JSON
    data = await response.json();
    return data;
  }
  onClick() {
    if (this.message.length > 0) {
      this.allMessages.push(this.message);
      this.message = "";
    }

  }
}
</script>
<style lang="scss" scoped>
#btn {
  margin-left: 40px;
}
#addBtn{
  margin-left: 50px;
}
#inputArea {
  width: 500px;
  height: 40px;
}
</style>
