using System;
using System.Collections.Generic;
using System.Data.Entity;
using System.Linq;
using System.Web;
using System.Web.Mvc;
using UMWebApplication.Models;

namespace UMWebApplication.Controllers
{
    public class ConfController : Controller
    {
        // GET: Conf
        public ActionResult Index()
        {
            using (UMWEBDBEntities1 aptadb = new UMWEBDBEntities1())
            {
                return View(aptadb.conferences.ToList());
            }
        }

        // GET: Conf/Details/5
        public ActionResult Details(int? id)
        {
            using (UMWEBDBEntities1 db = new UMWEBDBEntities1())
            {
                return View(db.conferences.Where(x => x.conference_number == id).FirstOrDefault());
            }
        }

        // GET: Conf/Create
        public ActionResult Create()
        {
            return View();
        }

        // POST: Conf/Create
        [HttpPost]
        public ActionResult Create(conference c)
        {
            try
            {
                using (UMWEBDBEntities1 ab = new UMWEBDBEntities1())
                {
                    ab.conferences.Add(c);
                    ab.SaveChanges();
                    //return View(aptadb.authortable.ToList());
                }

                return RedirectToAction("Index");
            }
            catch
            {
                return View();
            }
        }

        // GET: Conf/Edit/5
        public ActionResult Edit(int? id)
        {
            using (UMWEBDBEntities1 db = new UMWEBDBEntities1())
            {
                return View(db.conferences.Where(x => x.conference_number == id).FirstOrDefault());
            }
        }

        // POST: Conf/Edit/5
        [HttpPost]
        public ActionResult Edit(int? id, conference col)
        {
            try
            {
                using (UMWEBDBEntities1 a = new UMWEBDBEntities1())
                {
                    a.Entry(col).State = EntityState.Modified;
                    a.SaveChanges();
                }

                return RedirectToAction("Index");
            }
            catch
            {
                return View();
            }
        }

        // GET: Conf/Delete/5
        public ActionResult Delete(int? id)
        {
            using (UMWEBDBEntities1 b = new UMWEBDBEntities1())
            {
                return View(b.conferences.Where(x => x.conference_number == id).FirstOrDefault());
            }
        }

        // POST: Conf/Delete/5
        [HttpPost]
        public ActionResult Delete(int id, FormCollection collection)
        {
            try
            {
                using (UMWEBDBEntities1 ab = new UMWEBDBEntities1())
                {
                    conference co = ab.conferences.Where(x => x.conference_number == id).FirstOrDefault();
                    ab.conferences.Remove(co);
                    ab.SaveChanges();
                }

                return RedirectToAction("Index");
            }
            catch
            {
                return View();
            }
        }
    }
}
